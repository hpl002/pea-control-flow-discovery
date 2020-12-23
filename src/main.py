from flask import Flask
from swagger_ui import flask_api_doc

app = Flask(__name__)

flask_api_doc(app, config_path='../swagger.yaml',
              url_prefix='/api/doc', title='API doc')


@app.route('/api/')
def hello_world():
    return 'Hello, World!'
