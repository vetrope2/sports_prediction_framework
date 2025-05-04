from datawrapper.SportType import SportType
from dataloader.DataLoader import DataLoader
from transformer.Scope import *
from transformer.ScopeSelector import *
from transformer.Transformer import *
from transformer.DataSelector import *
from model.FlatModel import *
from learner.Learner import UpdatingLearner, Learner
from learner.Trainer import Trainer
from learner.Tester import Tester
from utils.TeamStrengthGraph import TeamStrengthGraph
from model.GNNModel import GNNModel
from sqlalchemy import or_


def filter_func(columns):
    return or_(columns.Lge == "ENG1", columns.Lge == "GER1")

func = lambda c: or_(c.Lge == "GER1", c.Lge == "GER1")
dw = DataLoader.load_and_wrap("isdb", "Matches", func, SportType.FOOTBALL)

t = Transformer()
dw = t.transform(dw)
graph_scope = EnumSelector(EnumScope())
graph = TeamStrengthGraph(graph_scope)
graph.compute(dw)
print(dw.get_dataframe())

relevant_scope = [EnumSelector(EnumScope()),WindowSelector(ScopeRoller(dw))]
prediction_scope = [EnumSelector(EnumScope()),WindowSelector(ScopeRoller(dw))]
scope = DataSelector(relevant_scope, prediction_scope)

gnn = GNNModel(graph)
l1 = Learner(Trainer(gnn), Tester(gnn), scope)
l = UpdatingLearner(Trainer(gnn), Tester(gnn), scope, [l1])
prob = l.compute(dw)
print(prob.get_dataframe())
