from sports_prediction_framework.datawrapper.SportType import SportType
from sports_prediction_framework.datawrapper.DataHandler import DataHandler
from sports_prediction_framework.dataloader.DataLoader import DataLoader
from sports_prediction_framework.transformer.Scope import *
from sports_prediction_framework.transformer.ScopeSelector import *
from sports_prediction_framework.transformer.Transformer import *
from sports_prediction_framework.transformer.DataSelector import *
from sports_prediction_framework.model.FlatModel import *
from sports_prediction_framework.learner.Learner import UpdatingLearner, LearnerWithoutScope
from sports_prediction_framework.learner.Trainer import Trainer
from sports_prediction_framework.learner.Tester import Tester
from sports_prediction_framework.utils.TeamStrengthGraph import TeamStrengthGraph
from sports_prediction_framework.model.GNNModel import GNNModel


try:
    df = pd.read_parquet('data.parquet')
except Exception as e:
    print(f"Failed to load parquet file: {e}")


df = df.head(200)
handler = DataHandler(df)
dw = SportType.FOOTBALL.get_wrapper()(handler)


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
l = LearnerWithoutScope(Trainer(gnn), Tester(gnn))

# 6. Run prediction and inspect output
prob = l.compute(dw)
print(prob)