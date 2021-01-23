import os
import json
import evaluator
import miner
import helper
from pathlib import Path
from flask import Flask, flash, request, redirect, url_for, Response, send_file, jsonify
from swagger_ui import flask_api_doc

UPLOAD_DIR_PATH = Path("./upload/").resolve()
DOWNLOAD_DIR_PATH = Path("./export/").resolve()
ALLOWED_EXTENSIONS = {"xes", "bpmn", "ptml"}

app = Flask(__name__)

# ENDPOINTS
flask_api_doc(app, config_path="./src/swagger.yaml",
              url_prefix="/api/doc", title="API doc")


@app.route("/api/discover", methods=["POST"])
def discover():
    if request.method == "POST":
        try:
            file = helper.is_correct_file(request.files, "log", "xes")
        except helper.HTTP_FileNotFoundError as e:
            return e.message, e.http
        helper.wipe_dir(UPLOAD_DIR_PATH)
        file.save(os.path.join(UPLOAD_DIR_PATH, file.filename))
        miner.mine(file.filename)
        export_fileName = helper.get_filename_from_dir(DOWNLOAD_DIR_PATH)
        return send_file(
            os.path.join(DOWNLOAD_DIR_PATH, export_fileName),
            attachment_filename=export_fileName,
            mimetype="text/xml",
            as_attachment=True,
        )


@ app.route("/api/translate/bpmn", methods=["POST"])
def translateBPMN():
    if request.method == "POST":
        try:
            file = helper.is_correct_file(request.files, "tree", "ptml")
        except helper.HTTP_FileNotFoundError as e:
            return e.message, e.http
        helper.wipe_dir(UPLOAD_DIR_PATH)
        file.save(os.path.join(UPLOAD_DIR_PATH, file.filename))
        miner.translateBPMN(file.filename)
        export_fileName = helper.get_filename_from_dir(DOWNLOAD_DIR_PATH)
        return send_file(
            os.path.join(DOWNLOAD_DIR_PATH, export_fileName),
            attachment_filename=export_fileName,
            mimetype="text/xml",
            as_attachment=True,
        )

@ app.route("/api/translate/petri", methods=["POST"])
def translatePetri():
    if request.method == "POST":
        try:
            file = helper.is_correct_file(request.files, "tree", "ptml")
        except helper.HTTP_FileNotFoundError as e:
            return e.message, e.http
        helper.wipe_dir(UPLOAD_DIR_PATH)
        file.save(os.path.join(UPLOAD_DIR_PATH, file.filename))
        miner.translatePetri(file.filename)
        export_fileName = helper.get_filename_from_dir(DOWNLOAD_DIR_PATH)
        return send_file(
            os.path.join(DOWNLOAD_DIR_PATH, export_fileName),
            attachment_filename=export_fileName,
            mimetype="text/xml",
            as_attachment=True,
        )        


@ app.route("/api/evaluate", methods=["POST"])
def evalaute():
    if request.method == "POST":
        try:
            # check if file exists
            log = helper.is_correct_file(request.files, "log", "xes")
            tree = helper.is_correct_file(request.files, "tree", "ptml")
        except helper.HTTP_FileNotFoundError as e:
            return e.message, e.http
        helper.wipe_dir(UPLOAD_DIR_PATH)
        path_tree = os.path.join(UPLOAD_DIR_PATH, "tree" + ".ptlm")
        path_log = os.path.join(UPLOAD_DIR_PATH, "log" + ".xes")
        # save files to dir
        tree.save(path_tree)
        log.save(path_log)

        try:
            funcs = json.loads(request.form.get("methods"))
            result = miner.evaluate(funcs, path_tree, path_log)
        except TypeError as e:
            return "could not find any methods in form", 400
        except Exception as e:
            return e.__traceback__, 500
        return result


@app.route("/api/rolediscovery", methods=["POST"])
def rolediscovery():
    if request.method == "POST":
        try:
            file = helper.is_correct_file(request.files, "log", "xes")
        except helper.HTTP_FileNotFoundError as e:
            return e.message, e.http
        helper.wipe_dir(UPLOAD_DIR_PATH)
        file.save(os.path.join(UPLOAD_DIR_PATH, file.filename))
        result = miner.mineforroles(file.filename)
        return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
