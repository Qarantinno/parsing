import logging
import os


if __name__ == '__main__':
    from sources.parsers import google_parse_place
    from util.utils import get_api_key, get_place_address_list, write_json

    api_key = get_api_key('google')
    places_info = list()
    for place in get_place_address_list('Green'):
        for k, v in place.items():
            logging.info('Will read {}'.format(k))
            places_info.append(google_parse_place(api_key, v))
    output_path = os.path.join(os.getcwd(), 'data/out.json')
    write_json(output_path, places_info)
