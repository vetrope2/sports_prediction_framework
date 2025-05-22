import mlflow


class MLFlowTracker:
    """
    A static MLflow tracker class to manage experiment runs and logging.

    This class uses class-level state to handle MLflow run lifecycle and logging
    without needing to instantiate objects.
    """
    _run = None

    @classmethod
    def set_experiment(cls, experiment_name: str) -> None:
        """
        Set the MLflow experiment to log runs to.

        Parameters
        ----------
        experiment_name : str
            The name of the MLflow experiment.
        """
        mlflow.set_experiment(experiment_name)

    @classmethod
    def start_run(cls, run_name: str = None) -> None:
        """
        Start a new MLflow run.

        Parameters
        ----------
        run_name : str, optional
            Optional name for the MLflow run (default is None).
        """
        cls._run = mlflow.start_run(run_name=run_name)

    @classmethod
    def log_params(cls, params: dict) -> None:
        """
        Log multiple parameters to the current MLflow run.

        Parameters
        ----------
        params : dict
            Dictionary of parameter names and values to log.

        Raises
        ------
        RuntimeError
            If called before starting a run.
        """
        if cls._run is None:
            raise RuntimeError("Start a run before logging params.")
        mlflow.log_params(params)

    @classmethod
    def log_metrics(cls, metrics: dict, step: int = None) -> None:
        """
        Log multiple metrics to the current MLflow run.

        Parameters
        ----------
        metrics : dict
            Dictionary of metric names and values to log.
        step : int, optional
            Optional step index for the metrics (default is None).

        Raises
        ------
        RuntimeError
            If called before starting a run.
        """
        if cls._run is None:
            raise RuntimeError("Start a run before logging metrics.")
        for k, v in metrics.items():
            mlflow.log_metric(k, v, step=step)

    @classmethod
    def end_run(cls) -> None:
        """
        End the current MLflow run if it exists.
        """
        if cls._run is not None:
            mlflow.end_run()
            cls._run = None