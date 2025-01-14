from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SelectPage(BasePage):
    NEXT_BUTTON = (By.CSS_SELECTOR, "button[data-autotest-next]")

    def select_frame(self, locator):
        self.click_radio_button(locator)

    def select_frames(self, locators: list):
        for locator in locators:
            self.click_radio_button(locator)

    def click_next_button(self):
        self.click(self.NEXT_BUTTON)

    def select_order_of_elements_and_click_next(self, ordered_elements):
        for element in ordered_elements:
            if isinstance(element, list):
                self.select_frames(element)
            else:
                self.select_frame(element)
            self.click_next_button()

    def input_and_click_next(self, locator, data):
        self.input_text(locator, data)
        self.click_next_button()
