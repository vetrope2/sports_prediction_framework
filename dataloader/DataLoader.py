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

    @classmethod
    def load_and_wrap_odds(cls, schema_name, table_name, filter_func, sport: SportType = None, bookmaker=None):
        ds = DataSource(sport)
        df = ds.query(schema_name, table_name, filter_func)


        bookie_func = lambda c: c.Bookmaker == bookmaker
        bets = ds.query_no_parse(schema_name, "Odds_1x2", bookie_func)
        bets = bets.rename(columns={"1": "odds_1", "X": "odds_X", "2": "odds_2"})


        cols_to_join = ["MatchID", "odds_1", "odds_X", "odds_2"]
        odds_subset = bets[cols_to_join]
        df = df.merge(odds_subset, on="MatchID", how="inner")
        df[["odds_1", "odds_X", "odds_2"]] = df[["odds_1", "odds_X", "odds_2"]].apply(pd.to_numeric, errors='coerce')

        handler = DataHandler(df)
        wrapper = sport.get_wrapper()(handler)
        ds.close()

        return wrapper
