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

Install the framework locally:

```bash
pip install .