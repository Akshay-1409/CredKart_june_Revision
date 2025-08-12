import logging
from pathlib import Path
import inspect

#base practice; dynamic, OS- independent Log file path
base_dir = Path(__file__).resolve().parent.parent
log_file_path = base_dir /"Logs" / "CredKart_automation.log"



class LoggerClass:
    @staticmethod
    def get_logger():
        log_file = logging.FileHandler(log_file_path)
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s -->  %(message)s")
        log_file.setFormatter(log_format)
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger




