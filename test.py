from dataloader.DataLoader import DataLoader
from dataloader.parser.SportType import SportType

"""c = Connector()
c.connect_to_db_via_ssh()


frame = pd.read_sql_query('SELECT * FROM "isdb"."Leagues" LIMIT 5;', con=c.eng)"""

#d = DataSource()
#df = d.plain_query('SELECT * FROM "isdb"."Leagues" LIMIT 5;')

#df = d.query_distinct( "isdb", "Leagues", lambda c: c.Country == "Australia")
#df = d.query_distinct( "isdb", "Leagues", lambda c: True, distinct_cols=["Country"])


#df = DataLoader.load("isdb", "Leagues", lambda c: True)

sport = SportType.SOCCER
func = sport.value().parse_isdb()

"""df = DataLoader.load("isdb", "Matches", lambda c: c.Lge == "GER1")
DL = MatchDL()
df = DL.parse_isdb(df)

print(df)"""

