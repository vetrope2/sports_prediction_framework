from datawrapper.SportType import SportType
from dataloader.DataLoader import DataLoader
from transformer.Scope import *
from transformer.ScopeSelector import *
from transformer.Transformer import *
from transformer.DataSelector import *
from model.FlatModel import *
from learner.Learner import *

"""c = Connector()
c.connect_to_db_via_ssh()


frame = pd.read_sql_query('SELECT * FROM "isdb"."Leagues" LIMIT 5;', con=c.eng)"""

#d = DataSource()
#df = d.plain_query('SELECT * FROM "isdb"."Leagues" LIMIT 5;')

#df = d.query_distinct( "isdb", "Leagues", lambda c: c.Country == "Australia")
#df = d.query_distinct( "isdb", "Leagues", lambda c: True, distinct_cols=["Country"])


#df = DataLoader.load("isdb", "Leagues", lambda c: True)

#WORKING
dw = DataLoader.load_and_wrap("isdb", "Matches", lambda c: c.Lge == "GER1", SportType.FOOTBALL)

init_parameters = {'col': 'Season', 'start': 2000, 'max': 2005, 'size': 1, 'stride': 2}

t = Transformer()
dw = t.transform(dw)

relevant_scope = [WindowSelector(ScopeRoller())]
prediction_scope = [WindowSelector(ScopeRoller())]
scope = DataSelector(relevant_scope, prediction_scope)
params = {'embed_dim': 32, 'out_dim': 3,'n_dense': 4,'dense_dim': 64,'architecture_type':'rectangle','batch_size':64,}
flat = FlatModel(params)
print(flat)
l = Learner(Trainer(flat), Tester(flat), scope)
prob = l.compute(dw)
print(prob.get_dataframe().head())
#print(t.base_transformer.id_map)
#print(dw.get_dataframe())







