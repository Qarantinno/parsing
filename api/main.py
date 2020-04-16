import logging
import os
import util.utils as util
import logging
import api.qarantino_api as api
import concurrent.futures

def apply_logging_config():
    logging.basicConfig(
        filename='output.log', 
        filemode='w', 
        level=logging.INFO, 
        format='%(threadName)s: %(levelname)s: %(asctime)s: %(message)s', 
        datefmt='%m/%d/%Y %I:%M:%S %p'
        )


def push_entry(entry):
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

if __name__ == '__main__':
    from sources.parsers import GoogleParser
    apply_logging_config()
    weekday = util.get_current_weekday()
    places_info = util._get_places_data_list()
    parser = GoogleParser(places_info)

    info = parser.parse_store_info()
    
    import psutil

    PROCNAME = "chrome"

    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()

    # for entry in info:
    #     push_entry(entry)

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as tpe:
        future_to_result = {tpe.submit(push_entry, entry): entry for entry in info}
        for future in concurrent.futures.as_completed(future_to_result):
            info_local = future_to_result[future]
            try:
                future.result()
            except Exception as e:
                logging.info(e)
        

    
