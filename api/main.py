import logging
import os
import util.utils as util


if __name__ == '__main__':
    from sources.parsers import GoogleParser
    weekday = util.get_current_weekday()
    places_info = util._get_places_data_list()
    parser = GoogleParser(places_info)
    out = {
        'day': weekday,
        'lives': parser.parse_store_info()
    }
    util.write_json(out)
    
