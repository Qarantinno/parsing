import logging
from .src.execution_tools.driver_pool import DriverPool
from .src.gui.pages.maps_result_page import GoogleMapsResultPage
from time import sleep
import pytz
from datetime import datetime


class GoogleParser:
    URL = 'https://www.google.com/maps/search/{0}'

    def __init__(self, places_info):
        self.places_info = places_info
        self.places = [place for place in places_info]
        self.driver = DriverPool().create_driver()
        
    
    def parse_store_info(self):
        info = list()
        try:
            for place in self.places:
                for address in place['addresses']:
                    result_page = GoogleMapsResultPage(self.driver, self.URL.format(place['name'] + ' ' + address))
                    result_page.open()
                    lives = result_page.get_search_result_live(address)
                    sleep(2)
                    abs_time = pytz.utc.localize(datetime.utcnow())
                    cur_time = abs_time.astimezone(pytz.timezone("Europe/Minsk")).isoformat()
                    coords = self.driver.current_url.split('/')[6].replace('@', '').replace('z', '').split(',')
                    info.append(
                        {
                            'name': place['name'],
                            'people': lives,
                            'datetime': cur_time,
                            'address': address,
                            'coords': {
                                'lat': coords[0],
                                'long': coords[1]
                            }
                        }
                    )
        except KeyboardInterrupt as e:
            self.driver.quit()

        self.driver.quit()
        return info

