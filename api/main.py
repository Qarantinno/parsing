import logging
import os
import util.utils as util
import logging


if __name__ == '__main__':
    from sources.parsers import GoogleParser
    logging.basicConfig(filename='output.log', filemode='w', level=logging.INFO, format='%(levelname)s: %(asctime)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    weekday = util.get_current_weekday()
    places_info = util._get_places_data_list()
    parser = GoogleParser(places_info)
    
    out = {
        'day': weekday,
        'lives': parser.parse_store_info()
    }
    util.write_json(out)
    
