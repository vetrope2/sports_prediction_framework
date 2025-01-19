# Sports Prediction Framework

## What is not yet finished:
- Currently the framework supports only one DataLoader operation andthat is from CSV. I will add loading through SQL, API and webscraping.
- The evaluation and simulation of betting strategies is not yet finished. I will have to study the theoretical concepts first (Kelly Growth etc.).
- Hyperparameter tuning is not yet implemented for the same reason as the previous.
- Exporting of reports or visualisation of data is not yet implemented.

# Components

## Model

Model is a class designed to simplify the training and prediction process of
machine learning models. It provides an easy-to-use interface for training a
model on a given dataset and making predictions based on new, unseen data.
The class supports various machine learning algorithms and allows users to
customize hyperparameters for optimal performance.

## DataLoader

DataLoader is an abstract base class (ABC) designed to serve as a blueprint for
loading data from various sources. This class is inherited by specialized classes
that handle data loading from different types of sources such as CSV files, SQL
databases, APIs, and web scrapers. The DataLoader class ensures consistency
in how data is loaded.

## DataWrapper

DataWrapper is a class designed to store and manage a pandas DataFrame while
providing an intuitive interface for data manipulation. It simplifies common
data operations such as filtering, aggregation, transformation, and visualization,
making it easier to work with structured datasets.

## DataTransformer
DataTransformer is a class designed to perform advanced data transformations
on pandas DataFrames. It provides functionality for outlier removal (based
on Z-score and IQR), data winsorization, and creating dummy variables for
categorical data. This class simplifies data preprocessing for machine learning
and statistical analysis workflows.

## Logger
Logger is a class designed to manage logging for a framework, providing detailed and customizable logs of system events, errors, and actions. This class is
an essential tool for monitoring, debugging, and understanding the framework
workflow.

## MLflowLogger
MLflowLogger is a class designed to streamline the process of logging models,
experiments, and metrics to MLflow. It provides a simple interface for tracking
and managing machine learning experiments, enabling better reproducibility,
performance monitoring, and version control

# Installation

```
pip install -r requirements.txt
```

# How to run
Run mlflow locally and then you are free to use the functions. An example is provided in a Jupyter notebook.
```cmd
mlflow ui
```

# Example

```python
from framework import CSVDataLoader

# Create a CSVDataLoader instance
csv_loader = CSVDataLoader()

# Load data into a DataWrapper
data = csv_loader.load_data('path/to/your/file.csv')

# Get the home_team column data
X = DataWrapper(data.get_data()['home_team'])
# Get the home_score data
y = data.get_data()['home_score']

dt = DataTransformer()
# Create dummies for categorical data
X = dt.create_dummies(X, 'home_team')

# Choose a modul you want
m = Model(RandomForestClassifier())

# Train and test
m.train_and_test(X.get_data(),y)
```
