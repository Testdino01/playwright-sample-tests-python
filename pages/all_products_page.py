from .base_page import BasePage
from playwright.sync_api import expect

class AllProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "all_products_title": '//h1[text()="All Products"]',
            "nth_product": '[href*="/product-detail/product"]',
            "nth_product_name": '[href*="/product-detail/product"] h2',
            "nth_product_price": '[href*="/product-detail/product"] p',
            "nth_product_review_count": '[href*="/product-detail/product"] h2 + div span.text-sm',
            "nth_product_wishlist_icon": '[aria-label="heart"]',
            "nth_product_wishlist_icon_count": '.bg-orange-100'
        }

    def assert_all_products_title(self):
        expect(self.page.locator(self.locators["all_products_title"])).to_be_visible()

    def get_nth_product(self, n):
        return self.page.locator(self.locators["nth_product"]).nth(n - 1)

    def click_nth_product(self, n):
        self.get_nth_product(n).click()

    def get_nth_product_name(self, n):
        return self.page.locator(self.locators["nth_product_name"]).nth(n - 1).text_content()

    def get_nth_product_price(self, n):
        return self.page.locator(self.locators["nth_product_price"]).nth(n - 1).text_content()

    def get_nth_product_review_count(self, n):
        return self.page.locator(self.locators["nth_product_review_count"]).nth(n - 1).text_content()

    def get_nth_product_wishlist_icon(self, n):
        return self.page.locator(self.locators["nth_product_wishlist_icon"]).nth(n - 1)

    def click_nth_product_wishlist_icon(self, n):
        self.get_nth_product(n).hover()
        self.get_nth_product_wishlist_icon(n).click()
        expect(self.page.get_by_text('Added to the wishlist')).to_be_visible()

    def get_nth_product_wishlist_icon_count(self, n):
        return self.page.locator(self.locators["nth_product_wishlist_icon_count"]).nth(n - 1)