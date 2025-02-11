from flask import Blueprint, jsonify
from app.services import search_accounts_from_platform, search_insights_for_account


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
    
    # PARA FAZER O /{{plataforma}} eu preciso:
    
    # - pegar todas as accounts da plataforma (api/accounts?platform=...)
    # - para cada account da plataforma
    # - pegar o id, name e token
    # - pegar todos os insights da account passando plataforma, id da account, token e fields (api/insights?platform=...)
        ## atenção porque os fields variam de acordo com a plataforma ##
    # - montar o relatório csv de acordo com as informações recebidas
    # - exportar o csv
    pass


def register_routes(app):
    app.register_blueprint(bp)
