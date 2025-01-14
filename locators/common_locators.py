from selenium.webdriver.common.by import By

class OwnerLocators:
    OWNER_YES_BUTTON = (By.CSS_SELECTOR, "input[data-autotest-owner-yes]")
    # ...other elements on the page...

class PersonalInfoLocators:
    FULLNAME_INPUT = (By.CSS_SELECTOR, "input[data-autotest-fullname-text]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-autotest-email-email]")
    # ...other elements on the page...

class PhoneNumberLocators:
    PHONE_NUMBER_INPUT = (By.CSS_SELECTOR, "input[data-autotest-phonenumber-tel]")
    SUBMIT_MY_REQUEST_BUTTON = (By.CSS_SELECTOR, "button[data-autotest-submit-my-request]")
    # ...other elements on the page...

class SquareFeetLocators:
    HOUSE_ARE_SQF_INPUT = (By.CSS_SELECTOR, "input[data-autotest-squarefeet-tel]")
    # ...other elements on the page...
