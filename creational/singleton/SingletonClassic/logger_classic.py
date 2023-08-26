import datetime
import os
from typing import TextIO


class Logger(object):
    log_file: TextIO

    @staticmethod
    def instance():
        if '_instance' not in Logger.__dict__:
            Logger._instance = Logger()
        return Logger._instance
    
    def open_log(self, path):
        self.log_file: TextIO = open(path, mode='a')
    
    def write_log(self, log_record):
        now: str = str(datetime.datetime.now())
        record: str = f'{now}: {log_record}\n'
        self.log_file.write(record)

    def close_log(self):
        self.log_file.close()


logger = Logger.instance()

current_script_path = os.path.dirname(os.path.abspath(__file__))
# parent_directory = os.path.dirname(current_script_path)
logger_path = os.path.join(current_script_path, 'singleton.log')

logger.open_log(logger_path)
logger.write_log('Logging with classic singleton pattern')
logger.close_log()
