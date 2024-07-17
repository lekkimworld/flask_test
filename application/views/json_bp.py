from flask import Blueprint, jsonify, current_app

json_bp = Blueprint("json_bp", __name__)

@json_bp.route("/<name>")
def json(name):
    key = current_app.config["SECRET_KEY"]
    return jsonify({"name": name, "secret": key})