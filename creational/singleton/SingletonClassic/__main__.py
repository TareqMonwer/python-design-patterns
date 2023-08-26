import os
from logger_classic import Logger


logger = Logger.instance()
current_script_path = os.path.dirname(os.path.abspath(__file__))
logger_path = os.path.join(current_script_path, 'singleton.log')

logger.open_log(logger_path)
logger.write_log('Logging with classic singleton pattern from __main__.py')
logger.close_log()
