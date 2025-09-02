from .base_page import BasePage
from playwright.sync_api import expect

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "shop_now_btn": '(//button[text()="Shop Now"])[1]',
            "all_products_title": '//h1[text()="All Products"]',
            "search_product_input": "input[placeholder='Search products...']",
            "select_product": '[class="relative pt-4 px-4"]',
            "product_title": '(//h1[text()="JBL Charge 4 Bluetooth Speaker"])[1]',
            "wishlist_icon": '//button[.//span[@aria-label="heart"]]',
            "all_products_link": "(//li[normalize-space()='All Products'])[1]",
            "add_to_cart_icon": "//*[name()='svg'][.//*[name()='path' and contains(@d,'M832 312H6')]]",
            "go_pro_hero10_black_title": "//h2[normalize-space()='GoPro HERO10 Black']",
            "continue_shopping_button": "//button[normalize-space()='Continue Shopping']",
            "wishlist_notification": 'div[role="status"][aria-live="polite"]:has-text("Added to the wishlist")',
            "wishlist_icon_header": '[data-testid="header-wishlist-count"]',
            "assert_wishlist_page": '[data-testid="wishlist-title"]',
            "wishlist_add_to_card": "//button[normalize-space()='Add to Cart']"
        }

    def click_on_shop_now_button(self):
        self.page.click(self.locators["shop_now_btn"])
        expect(self.page.locator(self.locators["all_products_title"])).to_be_visible()

    def search_product(self, product_name):
        self.page.fill(self.locators["search_product_input"], product_name)
        self.page.keyboard.press('Enter')

    def select_product(self):
        self.page.click(self.locators["select_product"])
        expect(self.page.locator(self.locators["product_title"])).to_be_visible()

    def add_to_wishlist(self):
        self.page.click(self.locators["wishlist_icon"])

    def assert_wishlist_icon(self):
        expect(self.page.locator(self.locators["wishlist_notification"])).to_be_visible()

    def click_on_wishlist_icon_header(self):
        self.page.locator(self.locators["wishlist_icon_header"]).click(force=True)

    def assert_wishlist_page(self):
        expect(self.page.locator(self.locators["assert_wishlist_page"])).to_be_visible()

    def click_on_wishlist_add_to_card(self):
        self.page.locator(self.locators["wishlist_add_to_card"]).click(force=True)

    def click_on_all_products_link(self):
        self.page.locator(self.locators["all_products_link"]).click(force=True)

    def click_on_add_to_cart_icon(self):
        self.page.locator(self.locators["add_to_cart_icon"]).click(force=True)

    def verify_product_title_visible(self, product_name):
        expect(self.page.locator(f'//h2[normalize-space()="{product_name}"]')).to_have_text(product_name)

    def click_on_continue_shopping(self):
        self.page.locator(self.locators["continue_shopping_button"]).click()
        # expect(self.page.locator(self.locators["all_products_title"])).to_be_visible()
        
        