from .base_page import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "home_nav": '//li[text()="Home"]',
            "about_us_nav": '//li[text()="About Us"]',
            "contact_us_nav": '//li[text()="Contact Us"]',
            "all_products_nav": '//li[text()="All Products"]',
            "shop_now_button": '//a[@href="/products"]/button[text()="Shop Now"]',
            "product_image": 'img[src="/products/Speaker.png"][alt="JBL Charge 4 Bluetooth Speaker"]',
            "add_to_cart_button": '[data-testid="add-to-cart-button"]',
            "add_cart_notification": 'div[role="status"][aria-live="polite"]:has-text("Added to the cart")',
            "price_range_slider2": '[data-testid="all-products-price-range-input-1"]',
            "price_range_slider1": '[data-testid="all-products-price-range-input-0"]',
            "filter_button": '[data-testid="all-products-filter-toggle"]',
            "about_us_title": '[data-testid="about-us-title"]'
        }

    def click_on_filter_button(self):
        self.page.locator(self.locators["filter_button"]).click()

    def adjust_price_range_slider(self, min_price, max_price):
        self.page.locator(self.locators["price_range_slider1"]).fill(min_price)
        self.page.locator(self.locators["price_range_slider2"]).fill(max_price)

    def click_on_shop_now_button(self):
        self.page.locator(self.locators["shop_now_button"]).click()

    def get_product_image(self):
        return self.page.locator(self.locators["product_image"])

    def click_product_image(self):
        self.get_product_image().click()

    def get_add_to_cart_button(self):
        return self.page.locator(self.locators["add_to_cart_button"])

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()

    def get_add_cart_notification(self):
        return self.page.locator(self.locators["add_cart_notification"])

    def validate_add_cart_notification(self):
        expect(self.get_add_cart_notification()).to_be_visible()

    def get_home_nav(self):
        return self.page.locator(self.locators["home_nav"]).first

    def get_about_us_nav(self):
        return self.page.locator(self.locators["about_us_nav"]).first

    def get_contact_us_nav(self):
        return self.page.locator(self.locators["contact_us_nav"]).first

    def get_all_products_nav(self):
        return self.page.locator(self.locators["all_products_nav"]).first

    def click_all_products_nav(self):
        self.get_all_products_nav().click()

    def get_shop_now_button(self):
        return self.page.locator(self.locators["shop_now_button"])

    def click_on_contact_us_link(self):
        self.get_contact_us_nav().click()

    def click_back_to_home_button(self):
        self.get_home_nav().click()

    def assert_home_page(self):
        expect(self.page.locator(self.locators["home_nav"])).to_be_visible(timeout=10000)

    def click_about_us_nav(self):
        self.get_about_us_nav().click()

    def assert_about_us_title(self):
        expect(self.page.locator(self.locators["about_us_title"])).to_be_visible(timeout=10000)