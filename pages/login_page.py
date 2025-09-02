from .base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "login_page_title": '//h2[text()=" Sign In"]',
            "user_name": '[placeholder="Your email address"]',
            "password": '[placeholder="Your password"]',
            "login_button": '//button[text()="Sign in"]',
            "invalid_login_error": '[data-test="error"]',
            "user_icon": '//*[name()="svg"][.//*[name()="path" and contains(@d,"M25.1578 1")]]',
            "logout_button": '//p[text()="Log Out"]',
            "signup_link": 'Sign up',
            "success_sign_in_message": 'Logged in successfully'
        }

    def navigate_to_login_page(self):
        self.navigate_to('/')

    def get_login_page_title(self):
        return self.page.locator(self.locators["login_page_title"])

    def get_user_name_input(self):
        return self.page.locator(self.locators["user_name"])

    def get_password_input(self):
        return self.page.locator(self.locators["password"])

    def get_login_button(self):
        return self.page.locator(self.locators["login_button"])

    def click_user_icon(self):
        self.page.locator(self.locators["user_icon"]).click()

    def click_on_user_profile_icon(self):
        self.page.locator(self.locators["user_icon"]).click()

    def assert_login_page(self):
        expect(self.get_login_page_title()).to_be_visible()
        expect(self.get_user_name_input()).to_be_visible()
        expect(self.get_password_input()).to_be_visible()
        expect(self.get_login_button()).to_be_visible()

    def login(self, username, password):
        self.page.fill(self.locators["user_name"], username)
        self.page.fill(self.locators["password"], password)
        self.page.click(self.locators["login_button"])
        self.page.wait_for_timeout(2000)

    def click_on_logout_button(self):
        self.page.locator(self.locators["logout_button"]).click()

    def validate_sign_in_page(self):
        expect(self.get_login_page_title()).to_be_visible()

    def click_on_signup_link(self):
        self.page.get_by_text(self.locators["signup_link"]).click()

    def verify_success_sign_in(self):
        expect(self.page.get_by_text(self.locators["success_sign_in_message"])).to_be_visible(timeout=10000)