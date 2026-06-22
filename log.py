import os
import logging

def logging_function(function_name: str, filename : str):

    #Create logs folder if not already created
    curr_folder = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(curr_folder, "log_entries")
    os.makedirs(log_dir, exist_ok = True)
    
    #Creates a logging object for the respective function
    logger = logging.getLogger(function_name)
    logger.setLevel(logging.DEBUG)

    #First check if log file is created for the respective function. If not then the log file is created
    #handler checks whether the logger object has been configured yet. If not then it creates a physical log file in the logs dir.
    if not logger.handlers:

        log_file_path = os.path.join(log_dir, f"{filename}.log")
        file_handler = logging.FileHandler(log_file_path)

        formatter = logging.Formatter(fmt = '%(filename)s_%(asctime)s --> %(message)s\n', datefmt = '%Y-%m-%d_%H:%M:%S')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    
    return logger