from .base_page import BasePage
from playwright.sync_api import expect
import os

class UserPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "user_icon": "//*[name()='svg'][.//*[name()='path' and contains(@d,'M25.1578 1')]]",
            "logout_button": "//p[text()='Log Out']",
            "address_tab": "(//*[@data-testid='menu-item-label'])[3]",
            "add_address_button": "[data-testid='add-new-address-button']",
            "add_new_address_menu": "//h2[text()='Add New Address']",
            "addressing_first_name": "[data-testid='first-name-input']",
            "addressing_email": "[data-testid='email-input']",
            "street_address": "[data-testid='street-address-input']",
            "city_input": "[data-testid='city-input']",
            "state_input": "[data-testid='state-input']",
            "country_input": "[data-testid='country-input']",
            "zip_code_input": "[data-testid='zip-code-input']",
            "save_address_button": "[data-testid='save-address-button']",
            "address_card_name": "[data-testid='address-name']",
            "edit_address_button": "(//*[@data-icon='edit'])[1]",
            "delete_address_button": "(//*[@data-icon='delete'])[1]",
            "confirm_delete_button": "//button[normalize-space(text())='Delete']",
            "update_address_button": "//button[text()='Update']",
            "first_name": "[name='firstname']",
            "last_name": "[name='lastName']",
            "contact_number": "[name='contactNumber']",
            "save_personal_info": "[aria-label='save']",
            "security_button": "//button[text()='Security']",
            "enter_new_password": "[placeholder='Enter new password']",
            "confirm_new_password": "[placeholder='Confirm your password']",
            "update_password_button": "[data-testid='my-profile-reset-password-button']",
            "update_notification": "div[role='status'][aria-live='polite']"
        }

    def click_on_user_profile_icon(self):
        self.page.locator(self.locators["user_icon"]).click()

    def click_on_address_tab(self):
        self.page.locator(self.locators["address_tab"]).click()

    def click_on_add_address_button(self):
        self.page.locator(self.locators["add_address_button"]).click()

    def check_add_new_address_menu(self):
        expect(self.page.locator(self.locators["add_new_address_menu"])).to_be_visible()

    def fill_address_form(self):
        self.page.locator(self.locators["addressing_first_name"]).fill('Tester')
        self.page.locator(self.locators["addressing_email"]).fill('testing123@example.com')
        self.page.locator(self.locators["street_address"]).fill('SBP, Utran')
        self.page.locator(self.locators["city_input"]).fill('Surat')
        self.page.locator(self.locators["state_input"]).fill('Gujarat')
        self.page.locator(self.locators["country_input"]).fill('India')
        self.page.locator(self.locators["zip_code_input"]).fill('12345')
        self.page.locator(self.locators["save_address_button"]).click()

    def verify_the_address_is_added(self):
        expect(self.page.locator(self.locators["address_card_name"])).to_be_visible()

    def click_on_edit_address_button(self):
        self.page.locator(self.locators["edit_address_button"]).click()

    def update_address_form(self):
        self.page.locator(self.locators["addressing_first_name"]).fill('Test1')
        self.page.locator(self.locators["addressing_email"]).fill('john.doe@example.com')
        self.page.locator(self.locators["street_address"]).fill('123 Main St')
        self.page.locator(self.locators["city_input"]).fill('Anytown')
        self.page.locator(self.locators["state_input"]).fill('CA')
        self.page.locator(self.locators["country_input"]).fill('United States')
        self.page.locator(self.locators["zip_code_input"]).fill('12345')
        self.page.locator(self.locators["update_address_button"]).click()

    def verify_the_updated_address_is_added(self):
        expect(self.page.locator(self.locators["address_card_name"])).to_contain_text('Test1')

    def click_on_delete_address_button(self):
        expect(self.page.locator(self.locators["address_card_name"])).to_contain_text('Test1')
        self.page.locator(self.locators["delete_address_button"]).click()
        self.page.locator(self.locators["confirm_delete_button"]).click()

    def update_personal_info(self):
        self.page.locator(self.locators["first_name"]).fill('Test1')
        self.page.locator(self.locators["last_name"]).fill('Testing')
        self.page.locator(self.locators["contact_number"]).fill('9999999999')
        self.page.locator(self.locators["save_personal_info"]).click()

    def verify_personal_info_updated(self):
        self.page.reload()
        expect(self.page.locator(self.locators["first_name"])).to_have_value('Test1')
        expect(self.page.locator(self.locators["last_name"])).to_have_value('Testing')
        expect(self.page.locator(self.locators["contact_number"])).to_have_value('9999999999')

    def click_on_security_button(self):
        self.page.locator(self.locators["security_button"]).click()

    def enter_new_password(self):
        self.page.locator(self.locators["enter_new_password"]).fill(os.getenv("NEW_PASSWORD"))

    def enter_confirm_new_password(self):
        self.page.locator(self.locators["confirm_new_password"]).fill(os.getenv("NEW_PASSWORD"))

    def click_on_update_password_button(self):
        self.page.locator(self.locators["update_password_button"]).click()

    def revert_password_back_to_original(self):
        self.page.locator(self.locators["enter_new_password"]).fill(os.getenv("PASSWORD"))
        self.page.locator(self.locators["confirm_new_password"]).fill(os.getenv("PASSWORD"))
        self.page.locator(self.locators["update_password_button"]).click()

    def get_update_password_notification(self):
        toast = self.page.locator(self.locators["update_notification"])
        expect(toast).to_be_visible()
        expect(toast).to_have_text("Password updated successfully")