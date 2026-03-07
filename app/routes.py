from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)


@bp.route("/ping")
def ping():
    print("function ping")
    return jsonify({"msg": "pong"})
