import os
import logging
from datetime import datetime
import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:
    def baseclass():
        pass
    
    def print_current_url(self):
        print("Current URL:", self.driver.current_url) 
        
    def get_logger(self):
        # Create log file with timestamp
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = os.path.join(log_dir, f"test_log_{current_time}.log")

        # Configure logger
        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler(log_file, mode='a')
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False
        return logger