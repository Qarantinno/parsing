from selenium.webdriver.common.by import By
from time import sleep

from sources.src.gui.elements.web_base_element import WebBaseElement
from sources.src.gui.elements.web_label import WebLabel
from sources.src.gui.elements.list.web_element_list import WebElementList
from sources.src.gui.elements.web_button import WebButton
from sources.src.gui.pages.base_page import BasePage
from sources.src.exceptions.exceptions import UIException


class GoogleMapsResultPage(BasePage):
    results = WebElementList(By.XPATH, "//div[@class='section-result']", WebButton)
    live_label = WebLabel(By.XPATH, "//div[@class='section-popular-times-value section-popular-times-live-value']")
    

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
    
    def get_page_url(self):
        return self.url

    def open(self):
        self.driver.get(self.url)

    def get_search_result_live(self, address):
        try:
            live_popularity = float(self.driver.find_element_by_xpath("//div[@class='section-popular-times-value section-popular-times-live-value']").get_attribute('style').split(':')[1].replace('px;', '').strip())
        except Exception as e:
            return
        return live_popularity

