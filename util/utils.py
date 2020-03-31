import os
import json
import logging
import copy


def get_api_key(service):
    parsers = {
        'google': read_google_parser_config
    }
    config = parsers[service]()
    key = None
    with open(config.get('api_key_path')) as f:
        key = f.readline()
    return key


def read_google_parser_config():
    """
    returns None if there's no google config
    """
    global_config = _read_global_config()
    parsers_config_list = global_config.get('parsers')
    logging.info('Will get google')
    google_config = dict()
    for parser_config in parsers_config_list:
        if parser_config.get('name') == 'google':
            google_config = copy.deepcopy(parser_config)
    return google_config


def get_place_address_list(name):
    place = _read_place_info_by_name(name)
    return place.get('addresses')


def _read_place_info_by_name(name):
    place_list = _get_places_data_list()
    place_info = dict()
    for place in place_list:
        if place.get('name') == name:
            place_info = copy.deepcopy(place)
    return place


def _get_places_data_list():
    places_config_path = os.path.join(
        os.getcwd(), 'config/places.json'
    )
    return _read_json(places_config_path)


def _read_global_config():
    global_config_path = os.path.join(
        os.getcwd(), 'config/global_settings.json'
    )
    return _read_json(global_config_path)


def write_json(path, obj):
    with open(path, 'w') as f:
        json.dump(obj, f)


def _read_json(path):
    with open(path) as f:
        return json.load(f)