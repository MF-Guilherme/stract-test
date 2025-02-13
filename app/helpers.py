import requests
from app.config import Config


def get_fields_by_platform(platform):
    fields = []
    page = 1
    while True:
        url = f"{Config.API_BASE_URL}/fields?platform={platform}&page={page}"
        headers = {"Authorization": Config.API_TOKEN}

        response = requests.get(url, headers=headers)
        data = response.json()

        if not data.get("fields"):
            break

        for field in data["fields"]:
            fields.append(field["value"])

        if "pagination" not in data or page >= data["pagination"].get("total", page):
            break

        page += 1

    return ",".join(fields)


def map_fields(insight, platform):
    # TODO - fazer com que os campos mapeados sejam dinâmicos e não fixos
    field_mapping = {
        'ga4': {
            'adName': 'ad_name',
            'region': 'country',
            'cost': 'spend'
        },
        'tiktok_insights': {
            'cost': 'spend'
        },
        'meta_ads': {
            'cpc': 'cost_per_click',
            'effective_status': 'status',
            'global_objective': 'objective'
        }
    }

    mapped_insight = {}
    for key, value in insight.items():
        if key in field_mapping.get(platform, {}):
            mapped_key = field_mapping[platform][key]
        else:
            mapped_key = key
        mapped_insight[mapped_key] = value

    return mapped_insight
