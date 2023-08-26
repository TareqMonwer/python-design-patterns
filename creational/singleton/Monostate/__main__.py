from creational.singleton.Monostate.singleton import Logger

logger = Logger("monostate_logger.log")
logger.write_log('Logging with monostate')

logger2 = Logger("IGNORED_FILE.log")

logger2.write_log('Just another log...')
logger.close_log()
logger2.close_log()