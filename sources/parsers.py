import logging
from .src.execution_tools.driver_pool import DriverPool
from time import sleep

driver_pool = DriverPool()

driver = driver_pool.create_driver()

logging.getLogger('ui').info('start')

driver.get('https://www.google.com/maps/search/%D0%B0%D0%BB%D0%BC%D0%B8')

sleep(10)

def gg():
    driver_pool = DriverPool()
    driver = driver_pool.create_driver()
    logging.getLogger('ui').info('start')
    driver.get('https://www.google.com/maps/search/%D0%B0%D0%BB%D0%BC%D0%B8')
    sleep(10)