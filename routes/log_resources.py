import json
from os import listdir
from os.path import isfile, join

from flask import request

from routes.common import init_logger
from constant import *


def get_list():
    logger = init_logger()
    log_path = LOG_PREFIX
    list_files = [f for f in listdir(log_path) if isfile(join(log_path, f))]
    logger.info(f'Received GET request')
    return {'data': list_files}


def get_log():
    logger = init_logger()
    logger.info(f'Received POST request')
    try:
        data = request.data
        date_read = json.loads(data)['date']

        filename = f'{LOG_PREFIX}/{date_read}'

        if not check_file_exist(filename):
            logger.error(f'{date_read} File not exist')
            return {'message': '{date_read} File not exist'}, 500

        with open(filename) as f:
            lines = f.read().splitlines()

        return {'data': lines}

    except Exception as e:
        logger.error(f'Something wrong: {e}')
        return {'message': f'Something wrong: {e}'}, 500


def check_file_exist(path):
    try:
        f = open(path)
        f.close()
        return True
    except FileNotFoundError:
        return False


if __name__ == '__main__':
    pass
