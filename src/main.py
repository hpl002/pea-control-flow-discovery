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
def allowed_file(filename, extentions):
    """[checks filename for allowed extension]

    Args:
        filename ([string]): [filename]
        extentions ([arr:string]): [arr of extensions, w/o dot]

    Returns:
        [type]: [boolean]
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in extentions


# ENDPOINTS
flask_api_doc(app, config_path='swagger.yaml',
              url_prefix='/api/doc', title='API doc')


@app.route('/api/discover', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 400, "No file found"
        file = request.files['file']
        if file.filename == '':
            return 400, "No filename found"
        if file and not allowed_file(file.filename, ["xes"]):
            return "Incompatible filetype. Expected .xes", 422
        ext = file.filename.rsplit('.', 1)[1].lower()
        helper.wipe_dir(UPLOAD_DIR_PATH)
        file.save(os.path.join(UPLOAD_DIR_PATH, "file"+"."+ext))
        message = miner.mine()
        export_fileName = helper.get_filename_from_dir(DOWNLOAD_DIR_PATH)
        return send_file(os.path.join(DOWNLOAD_DIR_PATH, export_fileName), attachment_filename=export_fileName, mimetype="text/xml")
