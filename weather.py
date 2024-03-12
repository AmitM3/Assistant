"""Function for weather details"""

import json

import requests

URL = "https://api.ims.gov.il/v1/envista/stations/178/data/latest"
headers = {"Authorization": "ApiToken f058958a-d8bd-47cc-95d7-7ecf98610e47"}
response = requests.request("GET", URL, headers=headers, timeout=20)
data = json.loads(response.text.encode("utf8"))


def weather():
    """Function for weather details."""
    temp = data["data"][0]["channels"][6]["value"]
    # rain = data["data"][0]["channels"][0]["value"]
    return f"the temprature in Ramat Gan right now is {temp} degrees"
