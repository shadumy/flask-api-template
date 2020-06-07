import jwt
from flask import jsonify, request

from constant import *
from routes.common import init_logger


def validate_token():
    try:
        logger = init_logger()
        req_secret = request.headers['SECRET']
        logger.info('Received a request. Checking the token key...')

        builder_secret_key = SECRET
        algorithm = ALGORITHM
        auth_body = AUTH_BODY

        decode = jwt.decode(req_secret, builder_secret_key, algorithm=algorithm)
        logger.info('Token key is valid...')

        if auth_body != decode['auth_body']:
            logger.error('Validate key false')
            return jsonify('UNAUTHORIZED'), UNAUTHORIZED
    except Exception as e:
        logger.error(f'UNAUTHORIZED: {e}')
        return jsonify(f'UNAUTHORIZED: {e}'), UNAUTHORIZED
