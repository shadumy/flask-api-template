from flask import Flask, request, Blueprint
from middleware.api_auth import validate_token
from routes.log_resources import get_list, get_log
from constant import *

app = Flask(__name__)
api = Blueprint('auth_api', __name__)


@app.route('/', methods=['GET', 'POST'])
def check_healthy():
    if request.method == 'POST':
        return request.json
    else:
        return 'Healthy!'


app.add_url_rule('/log', methods=['GET'], view_func=get_list)
app.add_url_rule('/log', methods=['POST'], view_func=get_log)

if REQUIRED_AUTH:
    app.before_request_funcs = {
        'auth_api': [validate_token]
    }
app.register_blueprint(api)

if __name__ == '__main__':
    # Development Environment
    app.run(debug=True, host='0.0.0.0', port=80)

    # Production Environment
    # serve(app, host='0.0.0.0', port='80')
