from datawrapper.SportType import SportType
from dataloader.DataLoader import DataLoader
from transformer.Scope import *
from transformer.ScopeSelector import *
from transformer.Transformer import *
from transformer.DataSelector import *
from model.FlatModel import *
from learner.Learner import *
from utils.TeamStrengthGraph import TeamStrengthGraph
from model.GNNModel import GNNModel
from sqlalchemy import or_


#WORKING
def filter_func(columns):
    return or_(columns.Lge == "ENG1", columns.Lge == "GER1")

func = lambda c: or_(c.Lge == "ENG1", c.Lge == "ENG1")
dw = DataLoader.load_and_wrap("isdb", "Matches", func, SportType.FOOTBALL)

t = Transformer()
dw = t.transform(dw)
print(dw.get_dataframe())
graph_scope = EnumSelector(EnumScope())
graph = TeamStrengthGraph(graph_scope)
graph.compute(dw)

relevant_scope = [EnumSelector(EnumScope()),WindowSelector(ScopeRoller(dw,{'col': 'Season', 'start': 2000, 'max': 2002, 'size': 50, 'stride': 2}))]
prediction_scope = [EnumSelector(EnumScope()),WindowSelector(ScopeRoller(dw, {'col': 'Season', 'start': 2002, 'max': 2004, 'size': 50, 'stride': 2}))]
scope = DataSelector(relevant_scope, prediction_scope)

gnn = GNNModel(graph)
l = Learner(Trainer(gnn), Tester(gnn), scope)
prob = l.compute(dw)
print(prob.get_dataframe())
