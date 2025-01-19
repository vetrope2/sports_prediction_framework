import logging

def setup_logger(name: str, log_file: str = None, level: int = logging.INFO) -> logging.Logger:
    """
    Setup and return a logger for the framework.

    :param name: Name of the logger.
    :param log_file: Optional path to a log file. If None, logs are only printed to the console.
    :param level: Logging level (default: logging.INFO).
    :return: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.hasHandlers():
        return logger

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler (if log_file is specified)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

# Initialize a global logger for the framework
framework_logger = setup_logger("FrameworkLogger", log_file="framework.log", level=logging.DEBUG)