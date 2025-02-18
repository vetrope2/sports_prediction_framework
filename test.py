from dataloader.Connector import Connector
import pandas as pd

ssh_host = "potato.felk.cvut.cz"  # Replace with actual SSH server
ssh_user = "vetrope2"
ssh_key_path = "~/.ssh/id_rsa"  # Replace with your SSH private key path

db_host = "147.32.83.171"  # PostgreSQL server's actual IP
db_port = 5432
db_name = "bet"
db_user = 'oganetig'
db_password = 'oganetig-fel-cvut-cz'

c = Connector()
c.connect_to_db_via_ssh()


frame = pd.read_sql_query('SELECT * FROM "isdb"."Leagues" LIMIT 5;', con=c.eng)
print(frame)
