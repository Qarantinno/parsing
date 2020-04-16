import logging
from .src.execution_tools.driver_pool import DriverPool
from .src.gui.pages.maps_result_page import GoogleMapsResultPage
from time import sleep
import pytz
from datetime import datetime
import itertools
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures


class GoogleParser:
    URL = 'https://www.google.com/maps/search/{0}'

    def __init__(self, places_info):
        self.places_info = places_info
        self.places = places_info
        self.pool = DriverPool()
        
    
    def parse_store_info(self):
        info = list()
        try:
            with ThreadPoolExecutor(max_workers=5) as tpe:
                future_to_result = {tpe.submit(self._read, place): place for place in self.places}
                for future in concurrent.futures.as_completed(future_to_result):
                    info_local = future_to_result[future]
                    try:
                        info.append(future.result())
                    except Exception as e:
                        logging.info(e)
                
        except KeyboardInterrupt as e:
            self.pool.kill_drivers()

        self.pool.kill_drivers()
        return list(itertools.chain(*info))

    def _read(self, place):
        driver = self.pool.create_driver()
        info = list()
        for address in place['addresses']:
            result_page = GoogleMapsResultPage(driver, self.URL.format(place['name'] + ' ' + address['address']))
            result_page.open()
        
            lives = result_page.get_search_result_live(address['address'])
        
            sleep(3)
            abs_time = pytz.utc.localize(datetime.utcnow())
            cur_time = abs_time.astimezone(pytz.timezone("Europe/Minsk")).isoformat()
            try:
                coords = driver.current_url.split('/')[6].replace('@', '').replace('z', '').split(',')
            except (IndexError) as e:
                continue
            info.append(
                {
                    'name': place['name'],
                    'people': lives,
                    'datetime': cur_time,
                    'address': address['address'],
                    'type': address['type'],
                    'modifier': address['modifier'],
                    'coords': {
                        'lat': coords[0],
                        'long': coords[1]
                    }
                }
            )
        return info

