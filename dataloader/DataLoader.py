from dataloader.DataSource import DataSource
from datawrapper.DataWrapper import DataWrapper
from datawrapper.DataHandler import DataHandler
from datawrapper.SportType import SportType
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

    @classmethod
    def preview(cls, schema_name: str, table_name: str, filter_func, distinct_cols=None) -> pd.DataFrame:
        ds = DataSource()
        df = ds.preview_query(schema_name, table_name, filter_func)
        ds.close()
        return df

    @classmethod
    def load_and_wrap(cls, schema_name, table_name, filter_func, sport: SportType = None):
        ds = DataSource(sport)
        df = ds.query(schema_name, table_name, filter_func)
        handler = DataHandler(df)
        wrapper = sport.get_wrapper()(handler)
        ds.close()

        return wrapper
