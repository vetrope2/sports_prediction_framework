from sports_prediction_framework.datawrapper.SportType import SportType
from sports_prediction_framework.dataloader.DataLoader import DataLoader
from sports_prediction_framework.transformer.Scope import *
from sports_prediction_framework.transformer.ScopeSelector import *
from sports_prediction_framework.transformer.Transformer import *
from sports_prediction_framework.transformer.DataSelector import *
from sports_prediction_framework.model.FlatModel import *
from sports_prediction_framework.learner.Learner import UpdatingLearner, Learner
from sports_prediction_framework.learner.Trainer import Trainer
from sports_prediction_framework.learner.Tester import Tester
from sports_prediction_framework.utils.TeamStrengthGraph import TeamStrengthGraph
from sports_prediction_framework.model.GNNModel import GNNModel
from sqlalchemy import or_



# 1. Filter data for Bundesliga and Premier League
def filter_func(columns):
    return or_(columns.Lge == "ENG1", columns.Lge == "GER1")

dw = DataLoader.load_and_wrap("isdb", "Matches", filter_func, SportType.FOOTBALL)

# 2. Transform data
t = Transformer()
dw = t.transform(dw)

# 3. Compute graph features
graph_scope = EnumSelector(EnumScope())
graph = TeamStrengthGraph(graph_scope)
graph.compute(dw)

# 4. Define scopes (Enum + Rolling Windows)
relevant_scope = [EnumSelector(EnumScope()), WindowSelector(ScopeRoller(dw))]
prediction_scope = [EnumSelector(EnumScope()), WindowSelector(ScopeRoller(dw))]
scope = DataSelector(relevant_scope, prediction_scope)

# 5. Initialize model and learners
gnn = GNNModel(graph)
l1 = Learner(Trainer(gnn), Tester(gnn), scope)
l = UpdatingLearner(Trainer(gnn), Tester(gnn), scope, [l1])

# 6. Run prediction and inspect output
prob = l.compute(dw)
print(prob.get_dataframe())
