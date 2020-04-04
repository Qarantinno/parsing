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