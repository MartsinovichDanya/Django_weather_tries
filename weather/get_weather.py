import requests


GEOCODER_URL = 'http://api.geonames.org/searchJSON'
WEATHER_SEARCH_URL = 'https://api.weather.yandex.ru/v1/informers'


def get_weather(city_name):
    city_search_params = {'name': city_name, 'maxRows': 1, 'username': 'danyamartsinovich'}
    city_data = requests.get(GEOCODER_URL, params=city_search_params).json()

    city_lat, city_lon = city_data['geonames'][0]['lat'], city_data['geonames'][0]['lng']

    weather_search_params = {'lat': city_lat, 'lon': city_lon, 'lang': 'ru_RU'}
    weather_data = requests.get(WEATHER_SEARCH_URL,
                                params=weather_search_params,
                                headers={'X-Yandex-API-Key': '1383a9b9-d016-433e-9b08-588fbe8368ab'}).json()
    return {
            'name': city_name,
            'temp': weather_data['fact']['temp'],
            'ftemp': weather_data['fact']['feels_like'],
            'icon': weather_data['fact']['icon']
            }
