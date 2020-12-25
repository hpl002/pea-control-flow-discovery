import os
import miner
import helper
from pathlib import Path
from flask import Flask, flash, request, redirect, url_for, Response, send_file
from swagger_ui import flask_api_doc

UPLOAD_DIR_PATH = Path('./upload/').resolve()
DOWNLOAD_DIR_PATH = Path('./export/').resolve()
ALLOWED_EXTENSIONS = {'xes', 'bpmn', 'ptml'}

app = Flask(__name__)


# HELPERS
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ENDPOINTS
flask_api_doc(app, config_path='swagger.yaml',
              url_prefix='/api/doc', title='API doc')


@app.route('/api/discover', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            ext = file.filename.rsplit('.', 1)[1].lower()
            helper.wipe_dir(UPLOAD_DIR_PATH)
            file.save(os.path.join(UPLOAD_DIR_PATH, "file"+"."+ext))
            message = miner.mine()
            return send_file('/', attachment_filename='ohhey.pdf')
            # return Response(message, status=200, mimetype='application/json')
