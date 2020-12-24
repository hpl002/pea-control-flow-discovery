import os
import miner
import helper
from pathlib import Path
from flask import Flask, flash, request, redirect, url_for, Response
from swagger_ui import flask_api_doc

UPLOAD_FOLDER = './upload/'
ALLOWED_EXTENSIONS = {'xes', 'bpmn', 'ptml'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# HELPERS
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ENDPOINTS
flask_api_doc(app, config_path='swagger.yaml',
              url_prefix='/api/doc', title='API doc')


# @app.route('/api')
# redirect("/api/doc")


@app.route('/api/discover', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            ext = file.filename.rsplit('.', 1)[1].lower()
            uploadDir = Path(app.config['UPLOAD_FOLDER']).resolve()
            # delete any existing file in upload dir
            helper.wipe_dir(uploadDir)
            file.save(os.path.join(uploadDir, "file"+"."+ext))
            message = miner.mine()
            return Response(message, status=200, mimetype='application/json')
