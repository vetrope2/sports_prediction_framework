from datawrapper.SportType import SportType
from dataloader.DataLoader import DataLoader
from transformer.Scope import *
from transformer.ScopeSelector import *
from transformer.Transformer import *

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
#print(t.base_transformer.id_map)
#print(dw.get_dataframe())







