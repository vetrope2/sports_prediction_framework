# Sports Prediction Framework

# Components

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

# Example

```python
from framework import CSVDataLoader

# Create a CSVDataLoader instance
csv_loader = CSVDataLoader()

# Load data into a DataWrapper
data_wrapper = csv_loader.load_data('path/to/your/file.csv')

# Access the pandas DataFrame
print(data_wrapper.data_frame)
```
