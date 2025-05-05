from datawrapper.SportType import SportType
from dataloader.DataLoader import DataLoader
from transformer.Scope import *
from transformer.ScopeSelector import *
from transformer.Transformer import *
from transformer.DataSelector import *
from model.FlatModel import *
from learner.Learner import Learner, UpdatingLearner, Tester, Trainer
from sqlalchemy import or_
from utils.Evaluation import evaluate_metrics

func = lambda c: or_(c.Lge == "GER1", c.Lge == "ENG1")
dw = DataLoader.load_and_wrap("isdb", "Matches", func, SportType.FOOTBALL)


t = Transformer()
dw = t.transform(dw)

train_params = {'col': 'Season', 'start': 2000, 'max': 2002, 'size': 1, 'stride': 1}
test_params = {'col': 'Season', 'start': 2000, 'max': 2002, 'size': 1, 'stride': 1}
relevant_scope = [WindowSelector(ScopeExpander(dw,train_params))]
prediction_scope = [WindowSelector(ScopeExpander(dw, test_params))]
scope = DataSelector(relevant_scope, prediction_scope)

model_params = {'embed_dim': 32, 'out_dim': 3,'n_dense': 4,'dense_dim': 64,'architecture_type':'rectangle','batch_size':64,}
flat = FlatModel(model_params)

l1 = Learner(Trainer(flat), Tester(flat), scope)
l = UpdatingLearner(Trainer(flat), Tester(flat), scope, [l1])
prob = l.compute(dw)


#print(prob.get_dataframe().head(400))
#print(prob.get_dataframe().loc[prob.get_dataframe()["Season"] == 2000])

df,matrix = evaluate_metrics(prob.get_dataframe(), 'macro')
print(df)

