from dataloader.Connector import Connector
from dataloader.parser.SportType import SportType
from dataloader.parser.AbstractParser import AbstractParser
import pandas as pd
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select


class DataSource:

    def __init__(self,sport_type: SportType = None, via_ssh=True):
        self.con = Connector()
        self.db_type = self.con.config['DB_NAME']

        if sport_type is not None:
            self.parser = sport_type.value()


        if via_ssh:
            self.con.connect_to_db_via_ssh()
        else:
            self.con.connect_to_db()



    def plain_query(self, query:str) -> pd.DataFrame:
        """
        Executes a raw SQL query provided in the query string. This method is dangerous
        because it directly interpolates user input into the SQL query string, which can lead
        to SQL injection attacks, since the input is not sanitized.
        """
        return pd.read_sql_query(query, con=self.con.get_engine())

    def parse_data(self, df: pd.DataFrame):
        match self.db_type:
            case "bet":
                pass
            case "flashscore":
                self.parser.parse_flashscore()



    def query(self, schema_name, table_name, filter_func) -> pd.DataFrame:
        metadata = MetaData(schema=schema_name)

        table = Table(table_name, metadata, autoload_with=self.con.eng, schema=schema_name)

        query = select(table).filter(filter_func(table.c))

        df = pd.read_sql(query, self.con.session.bind)

        return df

    def preview_query(self, schema_name, table_name, filter_func) -> pd.DataFrame:
        metadata = MetaData(schema=schema_name)

        table = Table(table_name, metadata, autoload_with=self.con.eng, schema=schema_name)

        query = select(table).filter(filter_func(table.c)).limit(5)

        df = pd.read_sql(query, self.con.session.bind)

        return df

    def query_distinct(self, schema_name, table_name, filter_func, distinct_cols=None) -> pd.DataFrame:
        """
        This function executes a SQL query that retrieves distinct rows based on a specific column,
        while returning all columns from the table.

        WARNING: This query uses PostgreSQL-specific feature `DISTINCT ON`.

        Arguments:
            schema_name (str): The schema of the table.
            table_name (str): The name of the table.
            filter_func (callable): A filter function to apply on the table's columns.
            distinct_cols (list): List of columns to apply DISTINCT ON.
        """
        metadata = MetaData(schema=schema_name)

        table = Table(table_name, metadata, autoload_with=self.con.eng, schema=schema_name)

        if distinct_cols:
            query = select(table).distinct(*[table.c[col] for col in distinct_cols]).filter(filter_func(table.c))
        else:
            query = select(table).filter(filter_func(table.c))

        df = pd.read_sql(query, self.con.session.bind)

        return df

    def close(self):
        self.con.close()
