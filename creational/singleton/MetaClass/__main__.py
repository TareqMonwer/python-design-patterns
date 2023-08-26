from creational.singleton.MetaClass.logger_meta import Logger

logger = Logger("meta_logger.log")
logger.write_log('Logging with metaclassed singleton')

logger2 = Logger("IGNORED_FILE.log")
assert logger2 is logger
print("Assertion passed.")

logger2.write_log('Just another log...')
logger.close_log()
logger2.close_log()