from random import randint

from lib.selenium_driver import Driver
from page_objects.registation.registration_locators import RegistrationLocators


class RegistrationPage(Driver):
    def register_account(self):
        self.type(f'goraved@{randint(1000, 99999)}.com', *RegistrationLocators.EMAIL_INPUT)
        self.click(*RegistrationLocators.CREATE_BTN)
        self.click(*RegistrationLocators.GENDER_OPTION)
        self.type('Test', *RegistrationLocators.CUSTOMER_FIRST_NAME_INPUT)
        self.type('Goraved', *RegistrationLocators.CUSTOMER_LAST_NAME_INPUT)
        self.type('123asd', *RegistrationLocators.PASSWORD_INPUT)
        self.select_by_value('1', *RegistrationLocators.DAYS_SELECTOR)
        self.select_by_value('1', *RegistrationLocators.MONTHS_SELECTOR)
        self.select_by_value('2020', *RegistrationLocators.YEARS_SELECTOR)
        self.click(*RegistrationLocators.AGREE_CHECKBOX)
        self.click(*RegistrationLocators.NEWSLETTER_CHECKBOX)
        self.type('Test', *RegistrationLocators.FIRST_NAME_INPUT)
        self.type('Goraved', *RegistrationLocators.LAST_NAME_INPUT)
        self.type('street', *RegistrationLocators.ADDRESS_INPUT)
        self.type('test', *RegistrationLocators.CITY_INPUT)
        self.select_by_value('1', *RegistrationLocators.STATE_SELECT)
        self.type('11111', *RegistrationLocators.POSTCODE_INPUT)
        self.type('123', *RegistrationLocators.OTHER_INPUT)
        self.type('123', *RegistrationLocators.PHONE_INPUT)
        self.click(*RegistrationLocators.ALIAS_BTN)
        self.click(*RegistrationLocators.SUBMIT_ACCOUNT_BTN)
