from sports_prediction_framework.datawrapper.SportType import SportType
from sports_prediction_framework.dataloader.DataLoader import DataLoader
import pandas as pd

dw = DataLoader.load_and_wrap_odds(
    "football",
    "Matches",
    lambda c: c.League == "Bundesliga",
    SportType.FOOTBALL,
    bookmaker="bet365"
)

dw.get_dataframe().to_parquet('data.parquet')

df_loaded = pd.read_parquet('data.parquet')
print(df_loaded)