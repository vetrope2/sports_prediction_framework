import paramiko
from sshtunnel import SSHTunnelForwarder
import psycopg2
from dotenv import load_dotenv, dotenv_values
from sqlalchemy import create_engine
from logger import framework_logger
import os

BASE_DIR = os.path.dirname(__file__)
dotenv_path = os.path.join(BASE_DIR, "..", ".env")

class Connector:
    def __init__(self):

        self.config = dotenv_values(dotenv_path)

    def connect_to_db(self):
        try:
            self.eng = create_engine(f'postgresql+psycopg2://{self.config["DB_USER"]}:{self.config["DB_PASSWORD"]}@127.0.0.1:5433/{self.config["DB_NAME"]}')
            framework_logger.info("Connected to database")
        except Exception as e:
            framework_logger.error("Connection to database failed.")
    def connect_to_db_via_ssh(self):

        try:
            # Establish SSH tunnel

            self.tunnel = SSHTunnelForwarder(
                (self.config['SSH_HOST'], 22),  # SSH server and port
                ssh_username=self.config['SSH_USER'],
                ssh_pkey=self.config['SSH_KEY_PATH'],
                remote_bind_address=(self.config['DB_HOST'], int(self.config['DB_PORT'])),  # Remote database address
                local_bind_address=('127.0.0.1', 5433)  # Local forwarding
            )

            self.tunnel.start()

            self.connect_to_db()
        except Exception as e:
            pass

    def close(self):
        self.tunnel.stop()
