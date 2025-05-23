from operator import or_

from sports_prediction_framework.dataloader.DataLoader import DataLoader
from sports_prediction_framework.datawrapper.SportType import SportType
from sports_prediction_framework.utils.Cache import Cache

# 1. Check if cached data wrapper file exists
if Cache.exists("cache/my_datawrapper.pkl"):
    # Load cached DataWrapper object
    wrapper = Cache.load("cache/my_datawrapper.pkl")
else:
    # Define filter function: Bundesliga or Premier League matches
    func = lambda c: or_(c.Lge == "GER1", c.Lge == "ENG1")

    # Load and wrap data with filtering and sport type
    wrapper = DataLoader.load_and_wrap("isdb", "Matches", func, SportType.FOOTBALL)

    # Save the wrapper to cache for future runs
    Cache.save(wrapper, "cache/my_datawrapper.pkl")


