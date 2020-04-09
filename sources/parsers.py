import logging
from .src.execution_tools.driver_pool import DriverPool
from .src.gui.pages.maps_result_page import GoogleMapsResultPage
from time import sleep


def gg(store):
    driver_pool = DriverPool()
    driver = driver_pool.create_driver()
    logging.getLogger('ui').info('start')
    url = 'https://www.google.com/maps/search/{0}'.format(store)
    page = GoogleMapsResultPage(driver, url)
    page.open()
    page.get_search_result_names()
    driver.quit()

class GoogleParser:
    URL = 'https://www.google.com/maps/search/{0}'

    def __init__(self, places_info):
        self.places_info = places_info
        self.places = [place for place in places_info]
        self.driver = DriverPool().create_driver()
        
    
    def parse_store_info(self):
        info = list()
        for place in self.places:
            for address in place['addresses']:
                result_page = GoogleMapsResultPage(self.driver, self.URL.format(place['name'] + ' ' + address))
                result_page.open()
                lives = result_page.get_search_result_live(address)
                info.append(
                    {
                        'name': place['name'],
                        'lives': lives,
                        'address': address
                    }
                )
        return info

