import os
from logger_base import Logger


logger = Logger("base_logger.log")
logger.write_log('Logging with base logger singleton')

logger2 = Logger("IGNORED_FILE.log")
assert logger2 is logger
print("Assertion passed.")

logger2.write_log('Just another log...')
logger.close_log()
