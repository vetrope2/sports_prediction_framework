from abc import ABC, abstractmethod
from datawrapper.DataWrapper import DataWrapper
from utils.AttributeSetter import AttributeSetter


class Scope(ABC):

    def __init__(self, wrapper: DataWrapper = None, parameters=None):
        self.wrapper = wrapper
        AttributeSetter.set_attributes(self, parameters)

    @abstractmethod
    def shift(self):
        pass

    @abstractmethod
    def inside(self):
        pass


class ScopeExpander(Scope):

    def shift(self):
        self.size += self.stride

    def inside(self):
        if self.start + self.size > self.max:
            return False
        return True


class ScopeRoller(Scope):

    def shift(self):
        self.start += self.stride

    def inside(self):
        if self.start > self.max:
            return False
        return True