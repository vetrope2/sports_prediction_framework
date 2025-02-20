from dataloader.DataSource import DataSource
import pandas as pd
class DataLoader:
    @classmethod
    def load(cls, schema_name: str, table_name: str, filter_func) -> pd.DataFrame:
        ds = DataSource()
        df = ds.query(schema_name, table_name, filter_func)
        ds.close()
        return df

    @classmethod
    def load_distinct(cls, schema_name: str, table_name: str, filter_func, distinct_cols=None) -> pd.DataFrame:
        ds = DataSource()
        df = ds.query(schema_name, table_name, filter_func)
        ds.close()
        return df

    def load_and_wrap(self, schema_name, table_name, filter_func):
        ds = DataSource()
        df = ds.query(schema_name, table_name, filter_func)
        ds.close()

        """ TO BE IMPLEMENTED"""

        return df
