import datetime
import os
from typing import Optional, TextIO
from creational.singleton.Monostate.borg import Borg


class Logger(Borg):
    log_file: Optional[TextIO] = None

    def __init__(self, path) -> None:
        if self.log_file is None:
            path = self.get_logger_path(path)
            self.log_file: Optional[TextIO] = open(path, mode='a')

    def write_log(self, log_record):
        now: str = str(datetime.datetime.now())
        record: str = f'{now}: {log_record}\n'
        if self.log_file is not None:
            self.log_file.write(record)

    def close_log(self):
        if self.log_file is not None:
            self.log_file.close()
        self.log_file: Optional[TextIO] = None

    def get_logger_path(self, path):
        current_script_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_script_path, path)
        return path
