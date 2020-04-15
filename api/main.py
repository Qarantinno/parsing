import logging
import os
import util.utils as util
import logging
import api.qarantino_api as api

if __name__ == '__main__':
    from sources.parsers import GoogleParser
    logging.basicConfig(filename='output.log', filemode='w', level=logging.INFO, format='%(levelname)s: %(asctime)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    weekday = util.get_current_weekday()
    places_info = util._get_places_data_list()
    parser = GoogleParser(places_info)

    info = parser.parse_store_info()
    for entry in info:
        if entry['people'] != -1:
            r = api.get_a_place(entry['address'])
            place_id = None
            if not r:
                p = api.post_a_place_payload
                p['name'] = entry['name']
                p['address'] = entry['address']
                p['type'] = entry['type']
                p['modifier'] = entry['modifier']
                p['coordinate']['lat'] = float(entry['coords']['lat'])
                p['coordinate']['lng'] = float(entry['coords']['long'])
                resp_place = api.post_a_place()
                place_id = id_place = resp_place['id']
            else:
                try:
                    place_id = r[0]['id']
                except IndexError as e:
                    place_id = r['id']
            s = api.post_a_shot_payload
            s['people']  = float(entry['people'])
            s['shotAt'] = entry['datetime']
            api.post_a_place_shot(place_id)
        

    
