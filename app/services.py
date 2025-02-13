import requests
from app.config import Config
from app.helpers import get_fields_by_platform, map_fields


def search_all_platforms():
    url = f"{Config.API_BASE_URL}/platforms"
    headers = {"Authorization": Config.API_TOKEN}

    response = requests.get(url, headers=headers)

    return response.json() if response.status_code == 200 else {"error", "Falha ao buscar as plataformas na api terceira"}


def get_platform_name(platform):
    platforms_response = search_all_platforms()
    platforms = platforms_response.get("platforms", [])
    for p in platforms:
        if p['value'] == platform:
            return p['text']
    return None


def search_accounts_from_platform(platform):
    all_accounts = []
    page = 1
    platform_name = get_platform_name(platform)
    while True:
        url = f"{Config.API_BASE_URL}/accounts?platform={platform}&page={page}"
        headers = {"Authorization": Config.API_TOKEN}

        response = requests.get(url, headers=headers)
        data = response.json()

        if not data.get("accounts"):
            break

        for account in data["accounts"]:
            account["platform_name"] = platform_name
            all_accounts.append(account)

        if "pagination" not in data or page >= data["pagination"].get("total", page):
            break

        page += 1

    return all_accounts


def search_insights_for_account(platform, account_id, token, fields=''):
    fields = get_fields_by_platform(platform)
    url = f"{Config.API_BASE_URL}/insights?platform={platform}&account={account_id}&token={token}&fields={fields}"
    headers = {"Authorization": Config.API_TOKEN}

    response = requests.get(url, headers=headers)
    insights = response.json() if response.status_code == 200 else {
        "error": "Falha ao buscar os insights na api terceira"}

    if "insights" in insights:
        insights["insights"] = [map_fields(
            insight, platform) for insight in insights["insights"]]

    return insights


def get_insights_by_account_name(plataforma):
    accounts = search_accounts_from_platform(plataforma)
    all_insights = []
    for account in accounts:
        insight = search_insights_for_account(
            plataforma, account['id'], account['token'])
        insight_with_name = {
            'platform': account['platform_name'],
            'account_name': account['name'],
            'insights': insight.get('insights', [])
        }
        all_insights.append(insight_with_name)
    return all_insights
