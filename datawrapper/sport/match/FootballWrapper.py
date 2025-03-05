from datawrapper.sport.MatchWrapper import MatchWrapper


class FootballWrapper(MatchWrapper):
    name = "Football"

    def __init__(self,data_handler=None):
        super().__init__(data_handler, home_advantage=True)