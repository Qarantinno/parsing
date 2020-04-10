from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep


from sources.src.gui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from sources.src.exceptions.exceptions import UIException

import logging

import re

from util.utils import get_current_weekday_code


class GoogleMapsResultPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
        self.regex = r'\b\d+(?:%|percent\b)'
    
    def get_page_url(self):
        return self.url

    def open(self):
        self.driver.get(self.url)

    def get_search_result_live(self, address):
        try:
            logging.info('{0} is being searched.'.format(address))
            live = WebDriverWait(self.driver, 3).until(getattr(EC, 'presence_of_element_located')((By.XPATH, "(//div[contains(@class, 'section-popular-times-current-value')])[{}]/..".format(get_current_weekday_code()))))
            s = live.get_attribute('aria-label')
            perc = re.search(self.regex, s).group(0)
            logging.info('{0}: found {1} popularity at the moment'.format(address, perc))
            live_popularity = float(perc.split('%')[0])
        except TimeoutException as ee:
            logging.info('{0}: nothing found, will return null'.format(address))
            return
        return live_popularity

