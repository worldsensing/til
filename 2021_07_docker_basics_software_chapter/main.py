import json

import requests

beer_api = "https://api.punkapi.com/v2/beers/9"


def get_info_beers():
    response_json = requests.get(beer_api).json()

    with open("/tmp/myjson.txt", "w") as text_file:
        text_file.write(json.dumps(response_json))

    return response_json


def sum(a, b):
    return a + b


print(f"HELLO: {sum(1, 2)}")

print(get_info_beers())
