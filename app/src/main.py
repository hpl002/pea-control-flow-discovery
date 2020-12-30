import os
import miner
import helper
from pathlib import Path
from flask import Flask, flash, request, redirect, url_for, Response, send_file
from swagger_ui import flask_api_doc

UPLOAD_DIR_PATH = Path("./upload/").resolve()
DOWNLOAD_DIR_PATH = Path("./export/").resolve()
ALLOWED_EXTENSIONS = {"xes", "bpmn", "ptml"}

app = Flask(__name__)

# ENDPOINTS
flask_api_doc(app, config_path="swagger.yaml",
              url_prefix="/api/doc", title="API doc")


@app.route("/api/discover", methods=["POST"])
def discover():
    if request.method == "POST":
        try:
            file = helper.is_correct_file(request.files, "log", "xes")
        except helper.HTTP_FileNotFoundError as e:
            return e.message, e.http
        ext = file.filename.rsplit(".", 1)[1].lower()
        helper.wipe_dir(UPLOAD_DIR_PATH)
        file.save(os.path.join(UPLOAD_DIR_PATH, "file" + "." + ext))
        miner.mine()
        export_fileName = helper.get_filename_from_dir(DOWNLOAD_DIR_PATH)
        return send_file(
            os.path.join(DOWNLOAD_DIR_PATH, export_fileName),
            attachment_filename=export_fileName,
            mimetype="text/xml",
            as_attachment=True,
        )


@app.route("/api/translate", methods=["POST"])
def translate():
    if request.method == "POST":
        file = helper.is_correct_file(request.files, "tree", "ptml")
        ext = file.filename.rsplit(".", 1)[1].lower()
        helper.wipe_dir(UPLOAD_DIR_PATH)
        file.save(os.path.join(UPLOAD_DIR_PATH, "file" + "." + ext))
        miner.translate()
        export_fileName = helper.get_filename_from_dir(DOWNLOAD_DIR_PATH)
        return send_file(
            os.path.join(DOWNLOAD_DIR_PATH, export_fileName),
            attachment_filename=export_fileName,
            mimetype="text/xml",
            as_attachment=True,
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
