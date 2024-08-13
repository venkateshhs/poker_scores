import logging
import os
from datetime import datetime


def get_logger(name: str) -> logging.Logger:
    """
    Creates and configures a logger that logs debug information to a file.

    The log file is saved in the `logs` directory with a name formatted as
    `poker_logs_{date_time_of_execution}.log`.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: Configured logger instance.
    """

    # Define the path for the logs directory within the current working directory
    log_dir = os.path.join(os.getcwd(), 'logs')

    # Create logs directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)

    # Generate the log file name with current date and time
    log_filename = f"poker_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_filepath = os.path.join('logs', log_filename)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_filepath)
    fh.setLevel(logging.DEBUG)

    # Create console handler for logging to the console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
