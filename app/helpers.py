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
