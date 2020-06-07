import logging
import logging.config
import datetime
from constant import *


def init_logger():
    date_time = str(datetime.date.today())
    logging.config.fileConfig(f'{PATH_PREFIX}/logging.ini',
                              defaults={'logfilename': f'{LOG_PREFIX}/{date_time}.log'})
    return logging.getLogger('apiLog')
