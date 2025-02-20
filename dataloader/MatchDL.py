from dataloader.DataLoader import DataLoader
import pandas as pd
import numpy as np


class MatchDL(DataLoader):
    def parse_flashscore(self, data: pd.DataFrame) -> pd.DataFrame:
        data = self.remove_not_valid_results(data)
        data = self.parse_score_PSQL(data)
        data = self.parse_season_PSQL(data)
        data = self.parse_date_PSQL(data)
        return data

    def parse_isdb(self, data: pd.DataFrame) -> pd.DataFrame:
        data.loc[data['WDL'] == "W", 'WDL'] = int(1)
        data.loc[data['WDL'] == "L", 'WDL'] = int(2)
        data.loc[data['WDL'] == "D", 'WDL'] = int(0)
        data = data.astype({'WDL': 'int32'})
        data.rename(columns={'HT': 'Home', 'AT': 'Away', 'GD': 'SD', 'Sea': 'Season', 'Lge': 'League'}, inplace=True)
        return data

    def remove_not_valid_results(self, data: pd.DataFrame):
        return data[(data["Result"] != '-') & (data["Result"] != '---')]

    def parse_score_PSQL(self, data: pd.DataFrame) -> pd.DataFrame:
        data["HS"] = pd.to_numeric(data["Result"].str.split("-", 1).str[0]).astype(np.int64)
        data["AS"] = pd.to_numeric(data["Result"].str.split("-", 1).str[1]).astype(np.int64)
        return data

    def parse_season_PSQL(self, data: pd.DataFrame) -> pd.DataFrame:
        data["Season"] = pd.to_numeric(data["Season"].str.split("/").str[0])
        return data

    def parse_date_PSQL(self, data: pd.DataFrame) -> pd.DataFrame:
        """ NOT IMPLEMENTED"""
        data[self.dateColumnName] = data["Time"].str.split(" ").str[0]
        return data