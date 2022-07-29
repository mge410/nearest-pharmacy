import json
import math


def lonlat_distance(a: float, b: float) -> float:
    """
    Определяем функцию,
    считающую расстояние между двумя точками,
    заданными координатами
    """

    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.0)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)
    return distance


def get_address(json_response: json) -> str:
    """Получаем адрес"""

    toponym = json_response['response']['GeoObjectCollection'][
        'featureMember'
    ][0]['GeoObject']
    toponym_coordinates = toponym['Point']['pos']
    return ','.join(toponym_coordinates.split(' '))


def get_pharmacy_info(json_response: json, address: str) -> dict:
    organization = json_response['features'][0]
    org_name = organization['properties']['CompanyMetaData']['name']
    org_address = organization['properties']['CompanyMetaData']['address']
    org_time = organization['properties']['CompanyMetaData']['Hours']['text']

    # Получаем координаты ответа.
    point = organization['geometry']['coordinates']
    org_point = '{0},{1}'.format(point[0], point[1])

    return {
        'адрес и название аптеки': ' - '.join([org_name, org_address]),
        'времени её работы': org_time,
        'расстояния до точки от исходной точки': lonlat_distance(
            list(map(float, org_point.split(','))),
            list(map(float, address.split(','))),
        ),
    }


def get_pharmacy_point(json_response: json) -> str:
    organization = json_response['features'][0]
    point = organization['geometry']['coordinates']
    return '{0},{1}'.format(point[0], point[1])
