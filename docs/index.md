# Sports Prediction Framework

Welcome to the **Sports Prediction Framework**, a modular and extensible Python framework designed to facilitate data handling, model training, evaluation, and betting simulations for sports analytics.

---

## Getting Started

- [Installation](installation.md)
- [Quick Start Guide](quickstart.md)
- [Core Concepts](core_concepts.md)
- [Examples](examples.md)


---

## Overview

This framework provides a comprehensive pipeline for sports prediction, including:

- **Data Loading & Parsing:** Flexible connectors and parsers to ingest and preprocess sports data from multiple sources.
- **Data Wrappers:** Clean abstractions over raw data for various sports and competitions, supporting feature extraction and label management.
- **Modeling:** Support for diverse predictive models, including flat and graph neural network architectures.
- **Training & Evaluation:** Learner, trainer, and tester components streamline the training process and enable robust model evaluation.
- **Simulation & Betting Strategies:** Implementations of multiple betting simulations to assess strategy performance using historical match data.
- **Optimization:** Integration with hyperparameter optimization tools to fine-tune model performance.
- **Data Transformation & Scoping:** Powerful mechanisms to segment and iterate over datasets for temporal or categorical analysis.

---

## Modules

- `dataloader`: Handles data ingestion and parsing.
- `datawrapper`: Wraps raw data into usable formats per sport.
- `model`: Contains model definitions and training logic.
- `learner`: Coordinates training and evaluation.
- `simulation`: Betting strategies and evaluation methods.
- `transformer`: Tools for data segmentation and transformation.
- `optimizer`: Hyperparameter tuning support.
- `utils`: Utility functions and helpers.






