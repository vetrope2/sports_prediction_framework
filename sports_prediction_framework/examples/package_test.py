import os
from sports_prediction_framework.datawrapper.SportType import SportType
from dotenv import load_dotenv, dotenv_values
sport = SportType.FOOTBALL

BASE_DIR = os.path.dirname(__file__)
dotenv_path = os.path.join(BASE_DIR, "..", "..", ".env")
print(dotenv_path)
config = dotenv_values(dotenv_path)
print(config["DB_NAME"])
