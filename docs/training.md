# Training Architecture: Trainer, Tester, and Learner

The training workflow in the framework is structured around three main components: **Trainer**, **Tester**, and **Learner**. This modular design promotes clear separation of responsibilities, flexibility, and ease of extension for different model types and evaluation strategies.

## Trainer

The **Trainer** is responsible for fitting a model to labeled training data. It acts as an interface between the data pipeline and the model’s training methods, ensuring that the appropriate input features and labels are passed. The Trainer handles all necessary preprocessing steps such as column selection and parameter preparation derived from the data. It supports a variety of model types, abstracting away internal model details.


## Tester

The **Tester** handles model evaluation by generating predictions on test or unseen datasets. It performs similar preprocessing to the Trainer, but instead of training, it routes data through the model’s prediction interface. The Tester also manages formatting and handling of prediction outputs to maintain a consistent evaluation interface across different model implementations.


## Learner

The **Learner** orchestrates the overall training and evaluation process by coordinating the Trainer, Tester, and a **DataSelector** component that defines data splits into training and testing scopes. It manages the training-evaluation loop, applying the Trainer to the training subset and the Tester to the corresponding testing subset.

### Variants of Learner

- **LearnerWithoutScope**  
  Designed for simple cases where no train/test split is necessary. Trainer and Tester operate on the same dataset directly.

- **UpdatingLearner**  
  Supports iterative training and evaluation workflows, such as rolling or sequential splits common in time-series or temporal datasets. It can manage multiple nested learners and merge their results using defined strategies.


