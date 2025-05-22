from operator import or_

from dataloader.DataLoader import DataLoader
from datawrapper.SportType import SportType
from utils.Cache import Cache

if Cache.exists("cache/my_datawrapper.pkl"):
    wrapper = Cache.load("cache/my_datawrapper.pkl")
else:
    func = lambda c: or_(c.Lge == "GER1", c.Lge == "ENG1")
    wrapper = DataLoader.load_and_wrap("isdb", "Matches", func, SportType.FOOTBALL)
    Cache.save(wrapper, "cache/my_datawrapper.pkl")


