import os
import json
import logging
import copy
import datetime


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


def get_current_weekday():
    weekdays_map = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    today = datetime.date.today()
    weekday = today.weekday()
    return weekdays_map[weekday]


def get_current_hour():
    time = datetime.datetime.now()
    return time.hour


def get_out_path():
    config = _read_global_config()
    return {
        'dir': config.get('ouput_dir_name'),
        'file': config.get('outfile')
    }


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


def write_json(obj):
    output_config = get_out_path()
    output_dir = output_config.get('dir')
    out_filename = output_config.get('file')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    with open(os.path.join(output_dir, out_filename), 'w') as f:
        json.dump(obj, f, indent=4)


def _read_json(path):
    with open(path) as f:
        return json.load(f)