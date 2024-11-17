import logging
import os
from datetime import datetime  # date and time for logging

# Create a log filename with current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # formatted timestamp

# Path to the 'logs' directory where log files will be saved
logs_directory = os.path.join(os.getcwd(), "logs")

# Create the 'logs' directory if it doesn't exist
os.makedirs(logs_directory, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE)

# Configure logging to log into the specified file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example usage of logging
logging.info("Logging setup is complete.")
