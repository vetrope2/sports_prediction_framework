import mlflow
import mlflow.sklearn  # Adjust for your model type

def log_mlflow_experiment(
    experiment_name: str,
    run_name: str,
    parameters: dict,
    metrics: dict,
    model=None,
    artifacts: dict = None,
):
    """
    Logs experiment details to a local MLflow server.

    :param experiment_name: Name of the MLflow experiment.
    :param run_name: Name of the specific run within the experiment.
    :param parameters: Dictionary of model parameters to log.
    :param metrics: Dictionary of performance metrics to log.
    :param model: Optional model object to log (e.g., sklearn model).
    :param artifacts: Optional dictionary of file paths for artifacts to log.
    """
    # Set the MLflow tracking URI to localhost
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run(run_name=run_name):
        # Log parameters
        if parameters:
            mlflow.log_params(parameters)

        # Log metrics
        if metrics:
            mlflow.log_metrics(metrics)

        # Log model (if provided)
        if model:
            mlflow.sklearn.log_model(model, artifact_path="model")

        # Log artifacts (if provided)
        if artifacts:
            for artifact_name, file_path in artifacts.items():
                mlflow.log_artifact(file_path, artifact_path=artifact_name)

        # Mark the run as successful
        mlflow.set_tag("status", "success")
