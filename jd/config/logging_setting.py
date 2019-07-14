import logging
import logging.config
import os

def get_logger(name='myAutoTest'):
    conf_log = os.path.join(os.path.dirname(os.path.abspath(__file__)),'logging.conf')
    logging.config.fileConfig(conf_log)
    logger = logging.getLogger(name)
    return logger


