from .base_page import BasePage
from playwright.sync_api import expect

class ContactUsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "contact_us_btn": '[data-testid="header-menu-contact-us"]',
            "contact_us_title": '[data-testid="contact-us-heading"]',
            "first_name_input": '[data-testid="contact-us-first-name-input"]',
            "last_name_input": '[data-testid="contact-us-last-name-input"]',
            "subject_input": '[data-testid="contact-us-subject-input"]',
            "message_input": '[data-testid="contact-us-message-input"]',
            "send_message_btn": '//button[@data-testid="contact-us-submit-button"]',
            "success_message": '[data-testid="contact-us-success-message"]'
        }

    def assert_contact_us_title(self):
        expect(self.page.locator(self.locators["contact_us_title"])).to_have_text('Contact Us')

    def fill_contact_us_form(self):
        self.page.fill(self.locators["first_name_input"], 'John')
        self.page.fill(self.locators["last_name_input"], 'Doe')
        self.page.fill(self.locators["subject_input"], 'Test Subject')
        self.page.fill(self.locators["message_input"], 'This is a test message.')
        self.page.click(self.locators["send_message_btn"])