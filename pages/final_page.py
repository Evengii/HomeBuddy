from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WeAreSorryPage(BasePage):
    GO_TO_HOMEPAGE_BUTTON = (By.XPATH, "//span[contains(text(), 'Go to homepage')]")

    def click_homepage_button(self):
        self.click_radio_button(self.GO_TO_HOMEPAGE_BUTTON)
    