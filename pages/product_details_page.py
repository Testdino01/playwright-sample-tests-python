from .base_page import BasePage
from playwright.sync_api import expect

class ProductDetailsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "plus_icon_to_add_quantity": "[aria-label='plus']",
            "total_quantity": "[aria-label='minus'] + div",
            "add_to_cart_button": "ADD TO CART",
            "header_cart_icon": "header-cart-icon",
            "product_additional_info_tab": "[data-testid='additional-info-tab']",
            "product_reviews_tab": "[data-testid='reviews-tab']",
            "write_review_btn": "//button[@data-testid='write-review-button']",
            "your_name_input": "[data-testid='review-form-name-input']",
            "email_input": "[data-testid='review-form-email-input']",
            "rating_stars": "[data-testid='review-form-rating-4']",
            "review_title_input": "[data-testid='review-form-title-input']",
            "give_your_opinion_input": "[data-testid='review-form-review-input']",
            "submit_btn": "[data-testid='review-form-submit-button']",
            "edit_review_btn": "[data-testid='edit-review-button']",
            "delete_review_btn": "[data-testid='delete-review-button']"
        }

    def assert_product_name_title(self, product_name):
        expect(self.page.locator(f"//h1[text()='{product_name}']").first).to_be_visible()

    def assert_product_review_count(self, product_name, product_review_count):
        expect(self.page.locator(f"//h1[text()='{product_name}']/following-sibling::div/p").first).to_contain_text(product_review_count)

    def assert_product_price(self, product_name, product_price):
        expect(self.page.locator(f"//h1[text()='{product_name}']/following-sibling::p[contains(@class, 'font-medium')]").first).to_contain_text(product_price)

    def get_plus_icon_to_add_quantity(self):
        return self.page.locator(self.locators["plus_icon_to_add_quantity"])

    def click_plus_icon_to_add_quantity(self):
        self.get_plus_icon_to_add_quantity().click()

    def get_total_quantity(self):
        return self.page.locator(self.locators["total_quantity"])

    def get_add_to_cart_button(self):
        return self.page.get_by_text(self.locators["add_to_cart_button"])

    def get_product_additional_info_tab(self):
        return self.page.locator(self.locators["product_additional_info_tab"])

    def get_product_reviews_tab(self):
        return self.page.locator(self.locators["product_reviews_tab"])

    def click_on_reviews_tab(self):
        self.get_product_reviews_tab().click()

    def assert_reviews_tab(self):
        expect(self.get_product_reviews_tab()).to_be_visible()

    def click_on_additional_info_tab(self):
        self.get_product_additional_info_tab().click()

    def assert_additional_info_tab(self):
        expect(self.get_product_additional_info_tab()).to_be_visible()

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        expect(self.page.get_by_text('Added to the cart')).to_be_visible()

    def get_cart_icon(self):
        return self.page.get_by_test_id(self.locators["header_cart_icon"])

    def click_cart_icon(self):
        self.get_cart_icon().click()

    def click_on_write_a_review_btn(self):
        self.page.locator(self.locators["write_review_btn"]).click()

    def fill_review_form(self):
        self.page.fill(self.locators["your_name_input"], 'John Doe')
        self.page.fill(self.locators["email_input"], 'testing@gmail.com')
        self.page.click(self.locators["rating_stars"])
        self.page.fill(self.locators["review_title_input"], 'Great Product')
        self.page.fill(self.locators["give_your_opinion_input"], 'This product exceeded my expectations. Highly recommend!')
        self.page.click(self.locators["submit_btn"])

    def assert_submitted_review(self, review):
        self.page.wait_for_timeout(3000)
        expect(self.page.locator(f"text={review['name']}")).to_be_visible()
        expect(self.page.locator(f"text={review['title']}")).to_be_visible()
        expect(self.page.locator(f"text={review['opinion']}")).to_be_visible()

    def click_on_edit_review_btn(self):
        self.page.locator(self.locators["edit_review_btn"]).click()

    def update_review_form(self):
        self.page.wait_for_timeout(3000)
        self.page.fill(self.locators["review_title_input"], 'Updated Review Title')
        self.page.fill(self.locators["give_your_opinion_input"], 'This is an updated review opinion.')
        self.page.click(self.locators["submit_btn"])

    def assert_updated_review(self, review):
        self.page.wait_for_timeout(3000)
        expect(self.page.locator(f"text={review['title']}")).to_be_visible()
        expect(self.page.locator(f"text={review['opinion']}")).to_be_visible()

    def click_on_delete_review_btn(self):
        self.page.locator(self.locators["delete_review_btn"]).click()
        self.page.get_by_text('Yes, Delete It').click() 

        