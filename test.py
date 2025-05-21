from datawrapper.SportType import SportType
from dataloader.DataLoader import DataLoader
from transformer.Scope import *
from transformer.ScopeSelector import *
from transformer.Transformer import *
from transformer.DataSelector import *
from model.FlatModel import *
from learner.Learner import Learner, UpdatingLearner, Tester, Trainer
from utils.TeamStrengthGraph import TeamStrengthGraph
from simulation.FlatBettingSimulation import FlatBettingSimulation

"""c = Connector()
c.connect_to_db_via_ssh()


frame = pd.read_sql_query('SELECT * FROM "isdb"."Leagues" LIMIT 5;', con=c.eng)"""

#d = DataSource()
#df = d.plain_query('SELECT * FROM "isdb"."Leagues" LIMIT 5;')

#df = d.query_distinct( "isdb", "Leagues", lambda c: c.Country == "Australia")
#df = d.query_distinct( "isdb", "Leagues", lambda c: True, distinct_cols=["Country"])


#df = DataLoader.load("isdb", "Leagues", lambda c: True)

#WORKING
dw = DataLoader.load_and_wrap_odds("football", "Matches", lambda c: c.League == "Bundesliga", SportType.FOOTBALL, bookmaker="bet365")
#dw = DataLoader.load_and_wrap("isdb", "Matches", lambda c: c.Lge == "GER1", SportType.FOOTBALL)



t = Transformer()
dw = t.transform(dw)


relevant_scope = [WindowSelector(ScopeExpander(dw,{'col': 'Season', 'start': 2015, 'max': 2018, 'size': 1, 'stride': 2}))]
prediction_scope = [WindowSelector(ScopeExpander(dw, {'col': 'Season', 'start': 2015, 'max': 2018, 'size': 1, 'stride': 2}))]
scope = DataSelector(relevant_scope, prediction_scope)
params = {'embed_dim': 32, 'out_dim': 3,'n_dense': 4,'dense_dim': 64,'architecture_type':'rectangle','batch_size':64,}
flat = FlatModel(params)
l1 = Learner(Trainer(flat), Tester(flat), scope)
l = UpdatingLearner(Trainer(flat), Tester(flat), scope, [l1])
prob = l.compute(dw)

sim = FlatBettingSimulation(prob)
sim.run()
sim.evaluate()
sim.summary()

#print(t.base_transformer.id_map)
#print(dw.get_dataframe())







