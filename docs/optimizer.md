# Optimizer

The `Optimizer` class provides a modular and extensible interface for hyperparameter tuning using the Optuna framework. It is designed to be agnostic to the internal model implementation, relying instead on a provided `Learner` instance and `DataWrapper` to orchestrate training and evaluation.

## Core Features

- **Learner-Agnostic**: Works with any `Learner` class, enabling use with a wide range of models.
- **Metric-Driven Optimization**: Selects the best hyperparameters using an evaluation metric of your choice.
- **Search Space Definition**: Accepts a flexible `search_space` dictionary with support for Optuna's parameter suggestion methods.
- **Robust Error Handling**: Supports pruning and failure skipping using Optuna's built-in mechanisms.
- **Repeatable & Configurable**: Fully configurable number of trials and seed for reproducibility.

## Optimization Workflow

The user provides:

   - A `Learner` class that wraps model training and testing.
   - A `DataWrapper` to supply training and testing data.
   - An `evaluate_metrics` function to compute a scalar score.
   - A `search_space` dictionary defining the parameters to optimize.

The optimizer iterates over trials:

   - It samples new hyperparameters using the search space.
   - Passes the parameters to the model through the learner.
   - Trains and tests the model.
   - Evaluates performance using the selected metric.
   - Logs and optionally prunes failed or suboptimal trials.

The best-performing set of parameters is returned at the end.

## Supported Metrics

The optimization process relies on a scoring function, typically selected from the following supported metrics:

| Metric         | Description                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------|
| **Accuracy**   | Measures the proportion of correct predictions among all predictions.                            |
| **Precision**  | Evaluates the number of true positives out of all predicted positives.                           |
| **Recall**     | Measures the number of true positives out of all actual positives.                               |
| **F1 Score**   | Harmonic mean of Precision and Recall, balancing false positives and false negatives.            |
| **Brier Score**| Quantifies the accuracy of probabilistic predictions (lower is better).                          |
| **RPS**        | Ranked Probability Score — evaluates the quality of multi-class probabilistic forecasts.         |

## Search Space Usage Example

```python
search_space = {
    'n_dense': ('int', 2, 5),
}

opt = Optimizer(datawrapper, learner, Metric.ACCURACY, search_space, n_trials=4)
opt.run()
```