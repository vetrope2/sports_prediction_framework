from enum import Enum
from dataloader.parser.MatchParser import MatchParser
from datawrapper.sport.match.FootballWrapper import FootballWrapper


class SportType(Enum):
    FOOTBALL = (MatchParser, FootballWrapper)


    def get_parser(self):
        return self.value[0]

    def get_wrapper(self):
        return self.value[1]
