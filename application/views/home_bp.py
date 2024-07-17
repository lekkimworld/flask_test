from flask import Blueprint

home_bp = Blueprint("home_bp", __name__)

@home_bp.route("/")
def home():
    return "<html><body><h1>Hello World!</h1></body></html>"