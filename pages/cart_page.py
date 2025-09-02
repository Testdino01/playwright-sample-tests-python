from .base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "your_cart_title": 'h2:has-text("Your Cart")',
            "cart_item_image": '[data-testid="cart-item-image"]',
            "cart_item_name": '[data-testid="cart-item-header"]',
            "cart_item_quantity": '[data-testid="item-quantity"]',
            "increase_quantity_button": '[data-testid="increase-quantity"]',
            "decrease_quantity_button": '[data-testid="decrease-quantity"]',
            "cart_item_price": '[data-testid="item-price"]',
            "remove_cart_item": '[data-testid="remove-item"]',
            "subtotal_label": '[data-testid="subtotal-label"]',
            "subtotal_value": '[data-testid="subtotal-value"]',
            "shipping_label": '[data-testid="shipping-label"]',
            "shipping_value": '[data-testid="shipping-value"]',
            "total_label": '[data-testid="total-label"]',
            "total_value": '[data-testid="total-value"]',
            "checkout_button": '[data-testid="checkout-button"]',
            "view_cart_button": '[data-testid="view-cart-button"]',
            "shopping_cart_icon": '[data-testid="header-cart-icon"]',
            "delete_item_button": '[aria-label="Remove item"]',
            "cart_empty": '[data-testid="empty-cart"]',
            "start_shopping_button": '[data-testid="continue-shopping-btn"]'
        }

    def assert_your_cart_title(self):
        expect(self.page.locator(self.locators["your_cart_title"])).to_be_visible(timeout=10000)

    def get_cart_item_image(self):
        return self.page.locator(self.locators["cart_item_image"])

    def get_cart_item_name(self):
        return self.page.locator(self.locators["cart_item_name"])

    def get_cart_item_quantity(self):
        return self.page.locator(self.locators["cart_item_quantity"])

    def get_increase_quantity_button(self):
        return self.page.locator(self.locators["increase_quantity_button"]).first

    def click_increase_quantity_button(self):
        self.page.locator(self.locators["increase_quantity_button"]).first.click()

    def get_decrease_quantity_button(self):
        return self.page.locator(self.locators["decrease_quantity_button"])

    def click_decrease_quantity_button(self):
        self.page.locator(self.locators["decrease_quantity_button"]).click()

    def get_cart_item_price(self):
        return self.page.locator(self.locators["cart_item_price"])

    def get_remove_cart_item(self):
        return self.page.locator(self.locators["remove_cart_item"])

    def get_subtotal_label(self):
        return self.page.locator(self.locators["subtotal_label"])

    def get_subtotal_value(self):
        return self.page.locator(self.locators["subtotal_value"])

    def get_shipping_label(self):
        return self.page.locator(self.locators["shipping_label"])

    def get_shipping_value(self):
        return self.page.locator(self.locators["shipping_value"])

    def get_total_label(self):
        return self.page.locator(self.locators["total_label"])

    def get_total_value(self):
        return self.page.locator(self.locators["total_value"])

    def get_checkout_button(self):
        return self.page.locator(self.locators["checkout_button"])

    def click_checkout_button(self):
        self.page.locator(self.locators["checkout_button"]).click()

    def get_view_cart_button(self):
        return self.page.locator(self.locators["view_cart_button"])

    def click_view_cart_button(self):
        self.page.locator(self.locators["view_cart_button"]).click()

    def click_on_cart_icon(self):
        self.page.locator(self.locators["shopping_cart_icon"]).click(force=True)

    def verify_cart_item_visible(self, product_name):
        expect(self.page.locator(self.locators["cart_item_name"])).to_be_visible()
        expect(self.page.locator(self.locators["cart_item_name"])).to_have_text(product_name)

    def click_on_checkout_button(self):
        self.page.wait_for_timeout(2000)
        self.page.locator(self.locators["checkout_button"]).click(force=True)

    def verify_increased_quantity(self, expected_quantity):
        expect(self.page.locator(self.locators["cart_item_quantity"])).to_have_text(expected_quantity)

    def click_on_delete_product_icon(self):
        self.page.locator(self.locators["delete_item_button"]).click()

    def verify_cart_item_deleted(self):
        expect(self.page.locator(self.locators["cart_item_name"])).to_have_count(0)

    def verify_empty_cart_message(self):
        expect(self.page.locator(self.locators["cart_empty"])).to_be_visible()