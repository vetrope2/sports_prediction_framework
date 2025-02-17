from dataloader.Connector import Connector

ssh_host = "potato.felk.cvut.cz"  # Replace with actual SSH server
ssh_user = "vetrope2"
ssh_key_path = "~/.ssh/id_rsa"  # Replace with your SSH private key path

db_host = "147.32.83.171"  # PostgreSQL server's actual IP
db_port = 5432
db_name = "bet"
db_user = 'oganetig'
db_password = 'oganetig-fel-cvut-cz'

c = Connector()
conn, tunnel = c.connect_to_db_via_ssh(ssh_host, ssh_user, ssh_key_path, db_host, db_port, db_name, db_user, db_password)

cursor = conn.cursor()
cursor.execute('SELECT * FROM "isdb"."Leagues" LIMIT 5;')  # Query the League table
rows = cursor.fetchall()

# Print column names
colnames = [desc[0] for desc in cursor.description]
print(f"Columns: {colnames}")

# Print rows
for row in rows:
    print(row)

cursor.close()