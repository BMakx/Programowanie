import requests
import json
size = '3500'
seed = '1764836658'
url = 'https://api.rustmaps.com/v4/maps/' + size + '/' + seed

header = {
    "Accept": "application/json",
    "X-API-Key": "5c3215cfabeb43da9200fb92e00dee40"
    }


response_API = requests.get(url=url, headers=header)
print(response_API.status_code)
