from transformer.Scope import Scope
from datawrapper.DataWrapper import DataWrapper
from abc import ABC, abstractmethod


class ScopeSelector(ABC):
    def __init__(self, scope: Scope) -> None:
        self.scope = scope

    @abstractmethod
    def transform(self, dataset: DataWrapper) -> DataWrapper:
        pass

    @abstractmethod
    def __str__(self):
        pass

    def update(self):
        self.scope.shift()

    def holds(self):
        return self.scope.inside()



class WindowSelector(ScopeSelector):

    def __init__(self, scope: Scope) -> None:
        super(WindowSelector, self).__init__(scope)

    def transform(self, dataset: DataWrapper) -> DataWrapper:
        data = dataset.get_dataframe()
        trans = data[(data[self.scope.col] >= self.scope.start) &
                     (data[self.scope.col] <= self.scope.start+self.scope.size)]
        return dataset.deepcopy(trans)

    def __str__(self):
        return str(self.scope.start) + ' ' + str(self.scope.start+self.scope.size)

    def current_state(self):
        return self.scope.current_state()