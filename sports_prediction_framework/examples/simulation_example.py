from sports_prediction_framework.datawrapper.SportType import SportType
from sports_prediction_framework.dataloader.DataLoader import DataLoader
from sports_prediction_framework.transformer.Scope import *
from sports_prediction_framework.transformer.Transformer import *
from sports_prediction_framework.transformer.DataSelector import *
from sports_prediction_framework.model.FlatModel import *
from sports_prediction_framework.learner.Learner import Learner, UpdatingLearner, Tester, Trainer
from sports_prediction_framework.simulation.FlatBettingSimulation import FlatBettingSimulation


# 1. Load Bundesliga data including bookmaker odds (bet365)
dw = DataLoader.load_and_wrap_odds(
    "football",
    "Matches",
    lambda c: c.League == "Bundesliga",
    SportType.FOOTBALL,
    bookmaker="bet365"
)

# 2. Transform data
t = Transformer()
dw = t.transform(dw)

# 3. Define training and prediction scopes with stride for rolling windows
relevant_scope = [WindowSelector(ScopeExpander(dw, {
    'col': 'Season', 'start': 2015, 'max': 2018, 'size': 1, 'stride': 2
}))]
prediction_scope = [WindowSelector(ScopeExpander(dw, {
    'col': 'Season', 'start': 2015, 'max': 2018, 'size': 1, 'stride': 2
}))]
scope = DataSelector(relevant_scope, prediction_scope)

# 4. Define model parameters and instantiate model
params = {
    'embed_dim': 32,
    'out_dim': 3,
    'n_dense': 4,
    'dense_dim': 64,
    'architecture_type': 'rectangle',
    'batch_size': 64,
}
flat = FlatModel(params)

# 5. Setup learner and updating learner
l1 = Learner(Trainer(flat), Tester(flat), scope)
l = UpdatingLearner(Trainer(flat), Tester(flat), scope, [l1])

# 6. Compute predictions
prob = l.compute(dw)

# 7. Run betting simulation with the predicted probabilities
sim = FlatBettingSimulation(prob)
sim.run()
sim.evaluate()
sim.summary()

