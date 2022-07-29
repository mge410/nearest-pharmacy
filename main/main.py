from io import BytesIO

from decouple import config
from PIL import Image
import requests

import core

SEARCH_API_SERVER = 'https://search-maps.yandex.ru/v1/'
GEOCODER_API_SERVER = 'http://geocode-maps.yandex.ru/1.x/'
MAP_API_SERVER = 'http://static-maps.yandex.ru/1.x/'

SEARCH_API_KEY = config('SEARCH_API_KEY', default='key')
GEOCODER_API_KEY = config('GEOCODER_API_KEY', default='key')

DELTA = '0.005'

toponym_to_find = input('Введите адрес от которого будем искать аптеку \n')

geocoder_params = {
    'apikey': GEOCODER_API_KEY,
    'geocode': toponym_to_find,
    'format': 'json',
}

geocoder_response = requests.get(GEOCODER_API_SERVER, params=geocoder_params)

if geocoder_response.status_code != 200:
    print('Ошибка запроса геокодера')
    raise SystemExit

address = core.get_address(geocoder_response.json())

search_params = {
    'apikey': SEARCH_API_KEY,
    'text': 'аптека',
    'lang': 'ru_RU',
    'll': address,
    'type': 'biz',
}

search_response = requests.get(SEARCH_API_SERVER, params=search_params)
if search_response.status_code != 200:
    print('Ошибка запроса поиска')
    raise SystemExit

pharmacy_info = core.get_pharmacy_info(search_response.json(), address)
pharmacy_point = core.get_pharmacy_point(search_response.json())

for key in pharmacy_info:
    print(key, ': ', pharmacy_info[key])

map_params = {
    'spn': ','.join([DELTA, DELTA]),
    'l': 'map',
    'pt': '{0},pm2rdl~{1},pm2dgl'.format(pharmacy_point, address),
}

response = requests.get(MAP_API_SERVER, params=map_params)
if search_response.status_code != 200:
    print('Ошибка запроса карт')
    raise SystemExit

Image.open(BytesIO(response.content)).show()
