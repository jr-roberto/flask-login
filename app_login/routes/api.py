from flask import Blueprint, jsonify

api = Blueprint('api',__name__, url_prefix="/api")

@api.route("/dados", methods=["GET"])
def dados():
    return jsonify({"msg":"Ola mundo"})
