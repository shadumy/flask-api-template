import logging
import logging.config
import datetime
from constant import *


def init_logger():
    logging.config.fileConfig(f'{PATH_PREFIX}/logging.ini',
                              defaults={'logfilename': f'{LOG_PREFIX}/' + str(
                                  datetime.date.today()) + '.log'})
    return logging.getLogger('apiLog')
