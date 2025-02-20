from dataloader.DataLoader import DataLoader
import pandas as pd

class RaceDL(DataLoader):
    def parse_flashscore(self, data: pd.DataFrame) -> pd.DataFrame:
        data = self.remove_not_valid_results(data)
        data = self.parse_score_PSQL(data)
        data = self.parse_date_PSQL(data)
        return data

    def remove_not_valid_results(self, data: pd.DataFrame):
        return data[data["Rank"].notnull()]

    def parse_date_PSQL(self, data: pd.DataFrame) -> pd.DataFrame:
        """TO BE IMPLEMENTED"""
        data[self.dateColumnName] = pd.to_datetime(data["Info"].str.split(" ").str[0])
        return data

    def parse_score_PSQL(self, data: pd.DataFrame):
        data['Rank'] = data['Rank'].str.replace('.', '')
        return data