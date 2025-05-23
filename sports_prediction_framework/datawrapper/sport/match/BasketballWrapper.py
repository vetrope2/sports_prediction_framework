from sports_prediction_framework.datawrapper.sport.MatchWrapper import MatchWrapper
from sports_prediction_framework.datawrapper.sport.LeagueWrapper import LeagueWrapper


class BasketballWrapper(MatchWrapper, LeagueWrapper):
    name = "Basketball"

    def __init__(self, data_handler=None):
        super().__init__(data_handler, home_advantage=True)