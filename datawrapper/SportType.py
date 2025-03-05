from enum import Enum
from dataloader.parser.MatchParser import MatchParser
from datawrapper.sport.match.FootballWrapper import FootballWrapper
from dataloader.parser.RaceParser import RaceParser
from datawrapper.sport.race.GolfWrapper import GolfWrapper


class SportType(Enum):
    FOOTBALL = (MatchParser, FootballWrapper)
    GOLF = (RaceParser, GolfWrapper)


    def get_parser(self):
        return self.value[0]

    def get_wrapper(self):
        return self.value[1]
