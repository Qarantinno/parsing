from selenium.webdriver.common.by import By
from time import sleep

from sources.src.gui.elements.web_base_element import WebBaseElement
from sources.src.gui.elements.web_label import WebLabel
from sources.src.gui.elements.list.web_element_list import WebElementList
from sources.src.gui.elements.web_button import WebButton
from sources.src.gui.pages.base_page import BasePage


class GoogleMapsResultPage(BasePage):

    results = WebElementList(By.XPATH, "//div[@class='section-result']", WebButton)
    back_btn = WebButton(By.XPATH, "//span[.='Back to results']")
    live_label = WebLabel(By.XPATH, "//div[@class='section-popular-times-value section-popular-times-live-value']")
    

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
    
    def get_page_url(self):
        return self.url

    def open(self):
        self.driver.get(self.url)

    def get_search_result_names(self):
        live_list = list()
        for _ in range(len(self.results._get_elements())):
            try:
                self.results._get_elements()[_].click()
                live_popularity = float(self.live_label.refind().get_attribute('style').split(':')[1].replace('px;', '').strip())
                live_list.append(live_popularity)
                self.back_btn.refind().click()
                sleep(1)
                self.driver.get(self.url)
            except Exception as e:
                print(e)
                self.driver.quit()
        print(live_list)

