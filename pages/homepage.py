from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomepagePage(BasePage):
    PROJECT_TYPE_SELECT = (By.CSS_SELECTOR, "select[data-autotest-verticals-options-list-header]")
