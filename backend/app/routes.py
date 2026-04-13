from flask import Blueprint, jsonify
from services.fetch_api import get_live_match

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return {"message": "API Running 🚀"}

@main.route("/match")
def match():
    return jsonify(get_live_match())