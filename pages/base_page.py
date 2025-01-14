from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(locator)).click()

    def click_radio_button(self, locator):
        element = WebDriverWait(self.driver, TIMEOUT).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text):
        WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_for_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
