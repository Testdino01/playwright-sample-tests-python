from .base_page import BasePage
from playwright.sync_api import expect

class SignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "signup_page_title": "//h2[text()=' Create Account']",
            "first_name": "#firstname",
            "last_name": "#lastname",
            "email": "#email",
            "password": "#password",
            "signup_button": "//button[text()='Create Account']",
            "success_signup_message": "Account created successfully! Please login to continue."
        }

    def navigate_to_signup_page(self):
        self.navigate_to('/signup')

    def get_signup_page_title(self):
        return self.page.locator(self.locators["signup_page_title"])

    def get_first_name_input(self):
        return self.page.locator(self.locators["first_name"])

    def get_last_name_input(self):
        return self.page.locator(self.locators["last_name"])

    def get_email_input(self):
        return self.page.locator(self.locators["email"])

    def get_password_input(self):
        return self.page.locator(self.locators["password"])

    def get_signup_button(self):
        return self.page.locator(self.locators["signup_button"])

    def assert_signup_page(self):
        expect(self.get_signup_page_title()).to_be_visible()
        expect(self.get_first_name_input()).to_be_visible()
        expect(self.get_last_name_input()).to_be_visible()
        expect(self.get_email_input()).to_be_visible()
        expect(self.get_password_input()).to_be_visible()
        expect(self.get_signup_button()).to_be_visible()

    def signup(self, first_name, last_name, email, password):
        self.page.fill(self.locators["first_name"], first_name)
        self.page.fill(self.locators["last_name"], last_name)
        self.page.fill(self.locators["email"], email)
        self.page.fill(self.locators["password"], password)
        self.page.locator(self.locators["signup_button"]).click()
        self.page.wait_for_timeout(2000)

    def verify_success_sign_up(self):
        expect(self.page.get_by_text(self.locators["success_signup_message"])).to_be_visible(timeout=10000)