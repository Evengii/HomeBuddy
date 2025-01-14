from locators.common_locators import SquareFeetLocators, OwnerLocators, PersonalInfoLocators, PhoneNumberLocators
from locators.hvac_locators import (ProjectTypeLocators, EquipmentLocators, EnergySourceLocators, EquipmentAgeLocators,
                                    PropertyTypeLocators)
from locators.select_page_locators import SelectPageLocators
from pages.estimation_page import HvacEstimationPage
from pages.select_page import SelectPage
from pages.final_page import WeAreSorryPage
from pages.homepage import HomepagePage
from data.test_data import UserData

from utils.config import HOMEPAGE_URL, BASE_URL


class TestUserScenario:
    def test_estimate_hvac(self, driver):
        estimation_page = HvacEstimationPage(driver)
        select_page = SelectPage(driver)
        final_page = WeAreSorryPage(driver)
        homepage = HomepagePage(driver)

        # Ordered tuple of locators in hvac estimation scenario
        hvac_elements = (
            ProjectTypeLocators.REPLACEMENT_BUTTON,
            [EquipmentLocators.AIR_CONDITIONER_BUTTON, EquipmentLocators.CENTRAL_HEATING_BUTTON],
            EnergySourceLocators.GAS_BUTTON,
            EquipmentAgeLocators.LESS_THAN_5_YEARS_BUTTON,
            PropertyTypeLocators.ROW_HOUSE_BUTTON,
        )

        estimation_page.fill_zip_code(code=10001)
        estimation_page.click_confirm_button()

        # Selecting options according to hvac scenario order
        select_page.select_order_of_elements_and_click_next(hvac_elements)

        # Square feet input step
        select_page.input_and_click_next(SquareFeetLocators.HOUSE_ARE_SQF_INPUT, UserData.generate_square())

        # Homeowner confirmation step
        select_page.select_frame(OwnerLocators.OWNER_YES_BUTTON)
        select_page.click_next_button()

        # Personal info page
        select_page.input_text(PersonalInfoLocators.FULLNAME_INPUT, UserData.generate_fullname())
        select_page.input_text(PersonalInfoLocators.EMAIL_INPUT, UserData.generate_email())
        select_page.click_next_button()

        # Phone number input step
        select_page.input_text(PhoneNumberLocators.PHONE_NUMBER_INPUT, UserData.generate_phone_number())
        select_page.click(PhoneNumberLocators.SUBMIT_MY_REQUEST_BUTTON)

        # Final page step
        assert select_page.wait_for_element(WeAreSorryPage.GO_TO_HOMEPAGE_BUTTON)
        final_page.click_homepage_button()
        assert driver.current_url == HOMEPAGE_URL
        assert homepage.wait_for_element(HomepagePage.PROJECT_TYPE_SELECT)

    def test_estimate_hvac_canceling(self, driver):
        estimation_page = HvacEstimationPage(driver)
        select_page = SelectPage(driver)

        estimation_page.fill_zip_code(code=10001)
        estimation_page.click_confirm_button()

        # Project type step
        select_page.select_frame(ProjectTypeLocators.REPLACEMENT_BUTTON)
        select_page.click_next_button()

        # Cancel project
        select_page.click(SelectPageLocators.CLOSE_BUTTON)
        select_page.click(SelectPageLocators.CANCEL_PROJECT_BUTTON)

        assert driver.current_url == BASE_URL
        assert estimation_page.wait_for_element(estimation_page.ZIP_CODE_INPUT)

    def test_estimate_hvac_cancel_disagree(self, driver):
        estimation_page = HvacEstimationPage(driver)
        select_page = SelectPage(driver)
        homepage = HomepagePage(driver)

        estimation_page.fill_zip_code(code=10001)
        estimation_page.click_confirm_button()

        # Project type step
        select_page.select_frame(ProjectTypeLocators.REPAIR_BUTTON)
        select_page.click(SelectPageLocators.NO_BUTTON)

        # Go to homepage
        select_page.click(SelectPageLocators.GO_TO_HOMEPAGE)

        assert driver.current_url == HOMEPAGE_URL
        assert homepage.wait_for_element(HomepagePage.PROJECT_TYPE_SELECT)
