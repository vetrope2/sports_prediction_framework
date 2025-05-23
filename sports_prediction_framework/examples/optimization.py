from sports_prediction_framework.datawrapper.SportType import SportType
from sports_prediction_framework.dataloader.DataLoader import DataLoader
from sports_prediction_framework.transformer.Scope import *
from sports_prediction_framework.transformer.ScopeSelector import *
from sports_prediction_framework.transformer.Transformer import *
from sports_prediction_framework.transformer.DataSelector import *
from sports_prediction_framework.model.FlatModel import *
from sports_prediction_framework.learner.Learner import Learner, UpdatingLearner, Tester, Trainer
from sqlalchemy import or_
from sports_prediction_framework.optimizer.Optimizer import Optimizer
from sports_prediction_framework.utils.Evaluation import Metric
from sports_prediction_framework.utils.Evaluation import evaluate_metrics

# 1. Load and filter data for Bundesliga matches
func = lambda c: c.Lge == "GER1"
dw = DataLoader.load_and_wrap("isdb", "Matches", func, SportType.FOOTBALL)

# 2. Transform the data
t = Transformer()
dw = t.transform(dw)

# 3. Define scopes for training and testing splits
train_params = {'col': 'Season', 'start': 2000, 'max': 2002, 'size': 1, 'stride': 1}
test_params = {'col': 'Season', 'start': 2000, 'max': 2002, 'size': 1, 'stride': 1}

relevant_scope = [WindowSelector(ScopeExpander(dw, train_params))]
prediction_scope = [WindowSelector(ScopeExpander(dw, test_params))]
scope = DataSelector(relevant_scope, prediction_scope)

# 4. Initialize model with fixed parameters
model_params = {
    'embed_dim': 32,
    'out_dim': 3,
    'n_dense': 4,
    'dense_dim': 64,
    'architecture_type': 'rectangle',
    'batch_size': 64,
}
flat = FlatModel(model_params)

# 5. Setup learners
l1 = Learner(Trainer(flat), Tester(flat), scope)
l = UpdatingLearner(Trainer(flat), Tester(flat), scope, [l1])

# 6. Define hyperparameter search space
search_space = {
    'n_dense': ('int', 2, 5),
}

# 7. Create optimizer and run search
opt = Optimizer(dw, l, Metric.ACCURACY, search_space, n_trials=4)
opt.run()

# 8. Output best parameters and metric
print("Best hyperparameters:", opt.best_params())
print("Best accuracy:", opt.best_value())