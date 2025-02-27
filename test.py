from dataloader.DataLoader import DataLoader

"""c = Connector()
c.connect_to_db_via_ssh()


frame = pd.read_sql_query('SELECT * FROM "isdb"."Leagues" LIMIT 5;', con=c.eng)"""

#d = DataSource()
#df = d.plain_query('SELECT * FROM "isdb"."Leagues" LIMIT 5;')

#df = d.query_distinct( "isdb", "Leagues", lambda c: c.Country == "Australia")
#df = d.query_distinct( "isdb", "Leagues", lambda c: True, distinct_cols=["Country"])


#df = DataLoader.load("isdb", "Leagues", lambda c: True)

df = DataLoader.preview("isdb", "Leagues", lambda c: True)
print(df)

