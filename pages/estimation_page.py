from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HvacEstimationPage(BasePage):
    ZIP_CODE_INPUT = (By.ID, "zipCode")
    GET_ESTIMATE_BUTTON = (By.CSS_SELECTOR, "button[data-autotest-zip-submit-0]")

    def fill_zip_code(self, code: int):
        self.input_text(self.ZIP_CODE_INPUT, code)

    def click_confirm_button(self):
        self.click(self.GET_ESTIMATE_BUTTON)
