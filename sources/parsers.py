import populartimes
import logging
import time
import os
from util.utils import get_api_key, get_current_hour, get_current_weekday, get_out_path, get_place_address_list


class IParser:
    def get_data(self, api_key, place_id):
        pass


class GoogleParser(IParser):

    def __init__(self, api_key, place_name):
        self.places_info = list()
        for place in get_place_address_list(place_name):
            for k, v in place.items():
                logging.info('Will read {}'.format(k))
                self.places_info.append(self.get_data(api_key, v))

    def get_data(self, api_key, place_id):
        return populartimes.get_id(api_key, place_id)

    def get_popular_times_today(self):
        current_weekday = get_current_weekday()
        current_hour = get_current_hour()
        popular_times_list = list()
        for place in self.places_info:
            popular_times_list.append(
                {
                'name': place['name'],
                'address': place['address'],
                'types': place['types'],
                'coordinates': place['coordinates'],
                'current_popularity': [day['data'] for day in place['populartimes'] if day['name'] == current_weekday][0][current_hour]
                }
            )
        return popular_times_list
