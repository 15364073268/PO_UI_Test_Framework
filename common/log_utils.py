import os
import logging


now_path = os.path.dirname(__file__)
log_path = os.path.join(now_path, '../logs/log.txt')


class LogUtils:

    def __init__(self, logfile_path=log_path):
        self.logfile_path = logfile_path
        self.logger = logging.getLogger()
        self.logger.setLevel(level=logging.INFO)
        file_log = logging.FileHandler(self.logfile_path)
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)


logger = LogUtils()


if __name__ == "__main__":
    log_utils = LogUtils()
    log_utils.info('你好李慧珍')