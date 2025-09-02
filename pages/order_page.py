from .base_page import BasePage
from playwright.sync_api import expect

class OrderPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "my_orders_tab": "//p[normalize-space()='My Orders']",
            "my_orders_title": "h2[data-testid='my-orders-title']",
            "view_details_button": "(//button[normalize-space()='View'])[1]",
            "order_details_title": "//h1[normalize-space()='Order Details']",
            "order_item_name": "p[data-testid='order-item-name']",
            "order_item_quantity": "p:has-text('Qty:')",
            "order_total_value": "p[data-testid='total-value']",
            "order_status_display": "div[class*='badge']",
            "cancel_order_button": "button:has-text('Cancel')",
            "confirm_cancellation_button": "//button[normalize-space()='Yes, Cancel Order']",
            "toaster_message": "div[id='_rht_toaster'] > div > div",
            "pagination_button": "//button[normalize-space()='{}']",
            "product_name_in_order_list": "h3[normalize-space()='{}']",
            "price_and_quantity_in_order_list": "div[normalize-space()='{}']",
            "order_status_in_list": "div[normalize-space()='{}']",
            "my_orders_count": "span[data-testid='my-orders-count']",
        }

    def click_on_my_orders_tab(self):
        self.page.locator(self.locators["my_orders_tab"]).click(force=True)

    def verify_my_orders_title(self):
        expect(self.page.locator(self.locators["my_orders_title"])).to_be_visible()

    def click_view_details_button(self, order_index=1):
        self.page.locator(f"(//button[normalize-space()='View'])[{order_index}]").click()

    def verify_order_details_title(self):
        expect(self.page.locator(self.locators["order_details_title"])).to_be_visible()

    def verify_order_summary(self, product_name, quantity, amount, status):
        expect(self.page.locator(self.locators["order_item_name"])).to_have_text(product_name)
        expect(self.page.locator(self.locators["order_item_quantity"])).to_contain_text(f"Qty: {quantity}")
        expect(self.page.locator(self.locators["order_total_value"])).to_contain_text(amount)
        expect(self.page.locator(self.locators["order_status_display"])).to_have_text(status)

    def click_cancel_order_button(self, button_index=2):
        self.page.locator(f"(//button[normalize-space()='Cancel'])[{button_index}]").click(force=True)

    def confirm_cancellation(self):
        self.page.locator(self.locators["confirm_cancellation_button"]).click(force=True)

    def verify_cancellation_confirmation_message(self):
        expect(self.page.locator(self.locators["toaster_message"])).to_be_visible()
        expect(self.page.locator(self.locators["toaster_message"])).to_contain_text('canceled successfully')

    def verify_order_status_is_canceled(self, product_name):
        badge_locator = f"//h3[normalize-space()='{product_name}']/ancestor::div[contains(@class, 'card')]//div[contains(@class, 'badge')]"
        expect(self.page.locator(badge_locator)).to_have_text('Canceled')

    def click_on_pagination_button(self, page_number):
        self.page.locator(self.locators["pagination_button"].format(page_number)).click(force=True)

    def verify_product_in_order_list(self, product_name):
        expect(self.page.locator(self.locators["product_name_in_order_list"].format(product_name))).to_be_visible()

    def verify_price_and_quantity_in_order_list(self, price_and_quantity):
        expect(self.page.locator(self.locators["price_and_quantity_in_order_list"].format(price_and_quantity))).to_be_visible()

    def verify_order_status_in_list(self, status, product_name):
        badge_locator = f"//h3[normalize-space()='{product_name}']/ancestor::div[contains(@class, 'card')]//div[contains(@class, 'badge')]"
        expect(self.page.locator(badge_locator)).to_have_text(status)

    def verify_my_orders_count(self):
        expect(self.page.locator(self.locators["my_orders_count"])).to_be_visible()