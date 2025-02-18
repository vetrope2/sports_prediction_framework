from dataloader.Connector import Connector
import pandas as pd


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


    def close(self):
        self.con.close()
