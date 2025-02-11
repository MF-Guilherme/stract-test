import requests
from app.config import Config
from app.utils import fields_by_platform


def search_all_platforms():
    url = f"{Config.API_BASE_URL}/platforms"
    headers = {"Authorization": Config.API_TOKEN}

    response = requests.get(url, headers=headers)

    return response.json() if response.status_code == 200 else {"error", "Falha ao buscar as plataformas na api terceira"}


def search_accounts_from_platform(platform):
    all_accounts = []
    page = 1

    while True:
        url = f"{Config.API_BASE_URL}/accounts?platform={platform}&page={page}"
        headers = {"Authorization": Config.API_TOKEN}

        response = requests.get(url, headers=headers)
        data = response.json()

        if not data.get("accounts"):
            break

        all_accounts.extend(data["accounts"])

        if "pagination" not in data or page >= data["pagination"].get("total", page):
            break

        page += 1

    return all_accounts


def search_insights_for_account(platform, account_id, token, fields=''):
    fields = fields_by_platform(platform)
    url = f"{Config.API_BASE_URL}/insights?platform={platform}&account={account_id}&token={token}&fields={fields}"
    headers = {"Authorization": Config.API_TOKEN}

    response = requests.get(url, headers=headers)

    return response.json() if response.status_code == 200 else {"error", "Falha ao buscar os insights na api terceira"}