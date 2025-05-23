from enum import Enum
from sports_prediction_framework.dataloader.parser.MatchParser import MatchParser
from sports_prediction_framework.datawrapper.sport.match.FootballWrapper import FootballWrapper
from sports_prediction_framework.dataloader.parser.RaceParser import RaceParser
from sports_prediction_framework.datawrapper.sport.race.GolfWrapper import GolfWrapper


class SportType(Enum):
    FOOTBALL = (MatchParser, FootballWrapper)
    GOLF = (RaceParser, GolfWrapper)


    def get_parser(self):
        return self.value[0]

    def get_wrapper(self):
        return self.value[1]
