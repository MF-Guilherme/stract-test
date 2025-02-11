from flask import Blueprint, jsonify
from app.services import search_all_platforms


bp = Blueprint("routes", __name__)

@bp.route("/", methods=["GET"])
def index():
    return jsonify({
        "name": "Guilherme Montenegro Ferreira",
        "email": "guimontenegro23@yahoo.com.br",
        "linkedin": "https://www.linkedin.com/in/guimontenegro/"
    })


def register_routes(app):
    app.register_blueprint(bp)
