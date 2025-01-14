from selenium.webdriver.common.by import By

class SelectPageLocators:
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[data-autotest-close]")
    YES_BUTTON = (By.CSS_SELECTOR, "button[data-autotest-yes]")
    NO_BUTTON = (By.CSS_SELECTOR, "button[data-autotest-no]")
    CANCEL_PROJECT_BUTTON = (By.CSS_SELECTOR, "button[data-autotest-cancel-project]")
    RETURN_TO_PROJECT_BUTTON = (By.CSS_SELECTOR, "button[data-autotest-return-to-project]")
    GO_TO_HOMEPAGE = (By.CSS_SELECTOR, "button[data-autotest-go-to-homepage]")
