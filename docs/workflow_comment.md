### 1. Load Bundesliga Data Including Bookmaker Odds (bet365)

In this step, we load Bundesliga match data filtered by league name and including bookmaker odds from "bet365". The data is wrapped for convenient use within the framework.

This method **shields the user from having to manually connect to a database or parse raw data based on the database format**. It returns a ready-to-use wrapped dataset for downstream tasks.
```python
# Load Bundesliga football match data with bet365 bookmaker odds
dw = DataLoader.load_and_wrap_odds(
    "football",
    "Matches",
    lambda c: c.League == "Bundesliga",
    SportType.FOOTBALL,
    bookmaker="bet365"
)
```
> **See Also:**  
> [DataLoader API Reference](reference/dataloader.md)
 
#### Excerpt of loaded data

| Date       | Home          | Away           | HS | AS | WDL | odds_1 | odds_X | odds_2 |
|------------|---------------|----------------|----|----|-----|--------|--------|--------|
| 2004-01-21 | Bayern Munich | Hamburger SV   | 3  | 0  | 1   | 1.39   | 4.00   | 6.50   |
| 2004-01-22 | Wolfsburg     | Dortmund       | 1  | 2  | 2   | 1.83   | 3.25   | 3.75   |
| 2004-01-22 | Nurnberg      | Kaiserslautern | 1  | 3  | 2   | 2.10   | 3.25   | 3.00   |
| 2004-01-22 | Nurnberg      | Kaiserslautern | 1  | 3  | 2   | 2.00   | —      | 3.25   |
| 2004-01-22 | Mainz         | Stuttgart      | 2  | 3  | 2   | 2.79   | 3.25   | 2.20   |


### 2. Apply Basic Transformations

In this step, we apply standard preprocessing transformations to the wrapped data using the framework’s `Transformer` class.

This step ensures that the raw data is cleaned and standardized for modeling. Transformations may include parsing dates, encoding categorical variables, or formatting numerical features.

```python
from sports_prediction_framework.transformer.Transformer import *
#Applies basic transformations to the dataframe.
t = Transformer()
dw = t.transform(dw)
print(dw)
```

By default, this transformation adds unique numeric identifiers for each team (Team ID columns), which are often used in embedding-based models.

#### Sample of Transformed Match Data

| Date       | Home           | Away            | HID | AID | HS | AS | WDL | odds_1 | odds_X | odds_2 |
|------------|----------------|------------------|-----|-----|----|----|-----|--------|--------|--------|
| 2004-01-21 | Bayern Munich  | Hamburger SV     |  5  | 17  |  3 |  0 |  1  |  1.39  |  4.00  |  6.50  |
| 2004-01-22 | Wolfsburg      | Dortmund         | 35  |  9  |  1 |  2 |  2  |  1.83  |  3.25  |  3.75  |
| 2004-01-22 | Nurnberg       | Kaiserslautern   | 27  | 24  |  1 |  3 |  2  |  2.10  |  3.25  |  3.00  |
| 2004-01-22 | Nurnberg       | Kaiserslautern   | 27  | 24  |  1 |  3 |  2  |  2.00  |   —    |  3.25  |
| 2004-01-22 | Mainz          | Stuttgart        | 26  | 32  |  2 |  3 |  2  |  2.79  |  3.25  |  2.20  |

> *Note: This is only a small sample of the available data. The full dataset contains additional rows and possibly other columns. Missing values are represented as em dashes (—).*

### 3. Define Training and Prediction Scopes

Before training, we define the scopes that determine which parts of the data will be used for training (relevant scope) and prediction (prediction scope). 

In this example, both scopes are created using `WindowSelector` combined with `ScopeExpander`, which slices the data by the 'Season' column, selecting windows starting from 2004 up to 2008 with a size of 1 season and a stride of 2 seasons.

The `DataSelector` then combines these scopes, managing the data segmentation for iterative training and testing.

```python
from sports_prediction_framework.transformer.Scope import *
from sports_prediction_framework.transformer.DataSelector import *

relevant_scope = [WindowSelector(ScopeExpander(dw, {
    'col': 'Season', 'start': 2004, 'max': 2008, 'size': 1, 'stride': 2
}))]
prediction_scope = [WindowSelector(ScopeExpander(dw, {
    'col': 'Season', 'start': 2004, 'max': 2008, 'size': 1, 'stride': 2
}))]
scope = DataSelector(relevant_scope, prediction_scope)
```

> **See Also:**  
> [Scope API Reference](reference/scope.md)
> 

### 4. Create Model and Setup Learner

Next, we instantiate a `FlatModel` with chosen parameters and configure a `Learner` and an `UpdatingLearner` to manage the training and evaluation process over the defined data scopes.

The `UpdatingLearner` supports iterative updates by coordinating one or more nested learners, enabling flexible training workflows.

```python
from sports_prediction_framework.model.FlatModel import FlatModel
from sports_prediction_framework.learner.Learner import Learner, UpdatingLearner, Tester, Trainer

params = {
    'embed_dim': 32,
    'out_dim': 3,
    'n_dense': 4,
    'dense_dim': 64,
    'architecture_type': 'rectangle',
    'batch_size': 64,
}
flat = FlatModel(params)

#Setup learner and updating learner
l1 = Learner(Trainer(flat), Tester(flat), scope)
l = UpdatingLearner(Trainer(flat), Tester(flat), scope, [l1])
```

### 5. Generate Predictions

After training, we use the learner to compute predictions on the dataset. The predicted probabilities for each outcome are stored in columns labeled `0`, `1`, and `2`.

This allows you to easily access the model’s confidence for each class or outcome.

```python
prob = l.compute(dw)
#Predictions stored in 0,1,2 columns.
print(prob)
```

#### Example Output

| Date       | Home          | Away          | HID | AID | HS | AS | WDL | odds_1 | odds_X | odds_2 | 1        | 0        | 2        |
|------------|---------------|---------------|-----|-----|----|----|-----|--------|--------|--------|----------|----------|----------|
| 2004-01-21 | Bayern Munich | Hamburger SV  | 5   | 17  | 3  | 0  | 1   | 1.39   | 4.00   | 6.50   | 0.596798 | 0.201601 | 0.201601 |
| 2004-01-22 | Wolfsburg     | Dortmund      | 35  | 9   | 1  | 2  | 2   | 1.83   | 3.25   | 3.75   | 0.174244 | 0.340452 | 0.485304 |
| 2004-01-22 | Nurnberg      | Kaiserslautern| 27  | 24  | 1  | 3  | 2   | 2.10   | 3.25   | 3.00   | 0.082314 | 0.082314 | 0.835371 |
| 2004-01-22 | Nurnberg      | Kaiserslautern| 27  | 24  | 1  | 3  | 2   | 2.00   |        | 3.25   | 0.082314 | 0.082314 | 0.835371 |
| 2004-01-22 | Mainz         | Stuttgart     | 26  | 32  | 2  | 3  | 2   | 2.79   | 3.25   | 2.20   | 0.031287 | 0.031287 | 0.937426 |



