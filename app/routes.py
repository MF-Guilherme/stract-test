from flask import Blueprint, jsonify
from app.utils import export_platform_report, export_collapsed_platform_report, export_general_report


bp = Blueprint("routes", __name__)


@bp.route("/", methods=["GET"])
def index():
    return jsonify({
        "name": "Guilherme Montenegro Ferreira",
        "email": "guimontenegro23@yahoo.com.br",
        "linkedin": "https://www.linkedin.com/in/guimontenegro/"
    })


@bp.route("/<plataforma>", methods=["GET"])
def platform_report(plataforma):
    return export_platform_report(plataforma)


@bp.route("/<plataforma>/resumo", methods=["GET"])
def resume_platform_report(plataforma):
    return export_collapsed_platform_report(plataforma)


@bp.route("/geral", methods=["GET"])
def general_report():
    return export_general_report()


def register_routes(app):
    app.register_blueprint(bp)
