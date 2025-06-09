# Sports Prediction Framework

A modular and extensible machine learning framework for predicting sports outcomes and evaluating betting strategies.

This framework enables seamless data ingestion, model training, prediction, and betting simulation for sports analytics. Designed for research, experimentation, and scalable deployment, it supports tabular and graph-based models, MLflow logging, and sophisticated evaluation tools.

## Features

- Support for multiple sports (e.g., matches and races)
- Plug-and-play architecture for custom data parsers, models, and strategies
- Built-in PyTorch-based models (`FlatModel`, `GNNModel`)
- MLflow integration for parameter and metric logging
- Iterative training and testing via customizable scopes
- Built-in betting strategy simulations (Kelly, Sharpe, Flat)
- Clean abstractions (`DataWrapper`, `Trainer`, `Learner`, etc.)
- Easily extendable for new formats, models, and evaluation methods


## Installation

Install the framework locally from the folder:

```bash
pip install .
```

Install from pypi:
```bash
pip install sports-prediction-framework
```

## Getting Started

Welcome to the framework! There are two main ways to get started depending on your setup and needs:

### 1. Connect to a Database

If you want to work with your own or a remote database, make sure to configure your environment by creating a `.env` file in your current working directory. This file should include your database credentials and, if necessary, SSH tunnel settings.

> See [Database Configuration](#using-database-data-in-the-framework) for detailed instructions.

### 2. Use the Self-Contained Examples

If you prefer a quick start without needing database access, you can explore our self-contained demonstrations. These run in Google Colab and use the sample data provided in the `examples` directory (`data.parquet`).

> Check out the [Examples and Demos](#self-contained-demonstration) to open the notebooks directly.

---

Feel free to choose the option that best fits your workflow. If you’re new, we recommend starting with the examples for a smooth introduction!


## Using Database Data in the Framework

To use data from a database within the framework, you **must** have a `.env` file located in your current working directory. This file should contain the necessary configuration variables for database connection.

### Required `.env` Variables

Below is an example of the essential variables your `.env` file should include:


```env
DB_HOST=your_db_host
DB_PORT=your_db_port
DB_NAME=your_db_name
DB_USER=your_db_username
DB_PASSWORD=your_db_password
```

> **⚠️ Warning:**  
> The following SSH-related variables are **only required** if you are connecting to the database via an SSH tunnel.


```env
SSH_HOST=ssh_server
SSH_USER=ssh_user
SSH_KEY_PATH=path_to_your_key
```


## Self-Contained Demonstration

We provide a self-contained demonstration that does **not** require any database access. This makes it easy to explore and test the framework without setting up a database connection.

The demonstration runs in **Google Colab** and uses the `data.parquet` file located in the `examples` directory of the repository.



You can open and run the notebooks directly via the following links:

- [Flat Model](https://colab.research.google.com/drive/1cvTSVJl9IKZ5zetAArQoUHMiGpkao_N1?usp=sharing)

- [Other Flat](https://colab.research.google.com/drive/1s_RPveoUixcFV2rnhW3lM3VRf8ynknlg?usp=sharing)

- [Model Evaluation](https://colab.research.google.com/drive/1h-C7imynYpMc1OvjwBnfxgcU2mvczJsb?usp=sharing)

- [Optimization](https://colab.research.google.com/drive/1PDxtwabuDKNq8BPbRyAJmk8nsWcuTvUy?usp=sharing)

- [Simulation example](https://colab.research.google.com/drive/18KNe19nwtR_dQaZLlF6deUjtP77b12B9?usp=sharing)

Feel free to explore these notebooks to get a hands-on understanding of the framework using real data samples.


### Example of `data.parquet` Content 

| Date       | Home          | Away           | HS | AS | WDL | odds_1 | odds_X | odds_2 |
|------------|---------------|----------------|----|----|-----|--------|--------|--------|
| 2004-01-21 | Bayern Munich | Hamburger SV   | 3  | 0  | 1   | 1.39   | 4.00   | 6.50   |
| 2004-01-22 | Wolfsburg     | Dortmund       | 1  | 2  | 2   | 1.83   | 3.25   | 3.75   |
| 2004-01-22 | Nurnberg      | Kaiserslautern | 1  | 3  | 2   | 2.10   | 3.25   | 3.00   |
| 2004-01-22 | Nurnberg      | Kaiserslautern | 1  | 3  | 2   | 2.00   | —      | 3.25   |
| 2004-01-22 | Mainz         | Stuttgart      | 2  | 3  | 2   | 2.79   | 3.25   | 2.20   |

> **Note:** This is a small excerpt of the `data.parquet` file. The actual dataset contains many more rows and columns with additional information.


## End-to-End Example

This example demonstrates how to:

- Load and filter data
- Apply a transformer
- Define training/testing scopes
- Initialize a model
- Run a learner with nested updating
- Obtain predictions

```python
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
```