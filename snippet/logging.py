# logging class
'''
수준	숫자 값
CRITICAL	50
ERROR	40
WARNING	30
INFO	20
DEBUG	10
NOTSET	0
'''

def _setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(name)
    logger.setLevel(level)


    file_handler = logging.FileHandler('./logs/flask.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def _change_logger_level(level):
    file_handler = logging.FileHandler('./logs/flask.log')
    logger.addHandler(file_handler)
