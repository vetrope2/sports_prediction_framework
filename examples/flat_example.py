from datawrapper.SportType import SportType
from dataloader.DataLoader import DataLoader
from transformer.Scope import *
from transformer.ScopeSelector import *
from transformer.Transformer import *
from transformer.DataSelector import *
from model.FlatModel import *
from learner.Learner import Learner, UpdatingLearner, Tester, Trainer
from sqlalchemy import or_


# 1. Load data with filter
func = lambda c: or_(c.Lge == "GER1", c.Lge == "ENG1")
dw = DataLoader.load_and_wrap("isdb", "Matches", func, SportType.FOOTBALL)

# 2. Transform the data
t = Transformer()
dw = t.transform(dw)

# 3. Define training and testing scopes
train_params = {'col': 'Season', 'start': 2000, 'max': 2002, 'size': 1, 'stride': 1}
test_params = {'col': 'Season', 'start': 2000, 'max': 2002, 'size': 1, 'stride': 1}

relevant_scope = [WindowSelector(ScopeExpander(dw, train_params))]
prediction_scope = [WindowSelector(ScopeExpander(dw, test_params))]
scope = DataSelector(relevant_scope, prediction_scope)

# 4. Define model parameters
model_params = {
    'embed_dim': 32,
    'out_dim': 3,
    'n_dense': 4,
    'dense_dim': 64,
    'architecture_type': 'rectangle',
    'batch_size': 64,
}
flat = FlatModel(model_params)

# 5. Define learners
l1 = Learner(Trainer(flat), Tester(flat), scope)
l = UpdatingLearner(Trainer(flat), Tester(flat), scope, [l1])

# 6. Run and get predictions
prob = l.compute(dw)
print(prob.get_dataframe())



