import logging
import os
from util.utils import write_json


if __name__ == '__main__':
    from sources.parsers import GoogleParser
    from util.utils import get_api_key

    api_key = get_api_key('google')
    place = 'Green'
    parser = GoogleParser(api_key, place)
    times = parser.get_popular_times_today()
    write_json(times)
