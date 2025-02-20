from dataloader.Connector import Connector
import pandas as pd
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select


class DataSource:

    def __init__(self, via_ssh=True):
        self.con = Connector()
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


    def query(self, schema_name, table_name, filter_func) -> pd.DataFrame:
        metadata = MetaData(schema=schema_name)

        table = Table(table_name, metadata, autoload_with=self.con.eng, schema=schema_name)

        query = select(table).filter(filter_func(table.c)).limit(5)

        df = pd.read_sql(query, self.con.session.bind)

        return df

    def close(self):
        self.con.close()
