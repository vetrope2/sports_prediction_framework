## `Model` Class

The `Model` class defines a standardized interface for all model implementations within the system. It serves as an abstract base, ensuring consistent usage and interchangeability across different modeling approaches.

### Methods

- **`fit(X, y)`**  
  Trains the model using input features `X` and target labels `y`.  
  This method must be implemented by all concrete subclasses.

- **`predict(X)`**  
  Generates predictions from the input features `X`.  
  Returns output in a consistent format, regardless of the model's internal structure.

- **`set_params(params)`**  
  Configures model hyperparameters dynamically using a dictionary `params`.  
  Enables flexible experimentation without requiring code changes.

- **`reset_state()`**  
  Resets or reinitializes the internal state of the model.  
  Useful for ensuring clean training or evaluation runs.

### Summary

These methods form the core interface contract for all models in the framework. By adhering to this interface, different model implementations can be easily integrated, compared, and swapped out within the system.
