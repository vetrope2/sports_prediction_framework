import paramiko
from sshtunnel import SSHTunnelForwarder
import psycopg2
from logger import framework_logger
class Connector:

    def connect(self, config_file: str):
        pass
    def connect_to_db_via_ssh(self, ssh_host, ssh_user, ssh_key_path, db_host, db_port, db_name, db_user, db_password):
        try:
            # Establish SSH tunnel
            tunnel = SSHTunnelForwarder(
                (ssh_host, 22),  # SSH server and port
                ssh_username=ssh_user,
                ssh_pkey=ssh_key_path,
                remote_bind_address=(db_host, db_port),  # Remote database address
                local_bind_address=('127.0.0.1', 5433)  # Local forwarding
            )
            tunnel.start()
            framework_logger.log("SSH tunnel established!")

            # Connect to PostgreSQL through the tunnel
            conn = psycopg2.connect(
                host="127.0.0.1",
                port=5433,
                dbname=db_name,
                user=db_user,
                password=db_password
            )
            framework_logger.log("Connected to PostgreSQL successfully!")
            return conn, tunnel
        except Exception as e:
            framework_logger.log(f"Connection failed: {e}")
            return None, None