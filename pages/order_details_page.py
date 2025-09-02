from .base_page import BasePage
from playwright.sync_api import expect

class OrderDetailsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "order_details_title": "order-details-title",
            "order_id": "order-id",
            "order_placed_name": "order-placed-name",
            "order_placed_message": "order-placed-message",
            "order_placed_date": "order-placed-date",
            "back_to_home_button": "back-to-home",
            "order_information": {
                "order_information_title": "order-information-title",
                "order_confirmed_title": "order-confirmed-title",
                "order_confirmed_message": "order-confirmed-message",
                "shipping_details_title": "shipping-details-title",
                "shipping_email_value": "shipping-email-value",
                "payment_method_amount": "payment-method-amount",
                "delivery_address_label": "delivery-address-label",
                "delivery_address_value": "delivery-address-value",
                "continue_shopping_button": "continue-shopping-button"
            },
            "order_summary": {
                "order_summary_title": "order-summary-title",
                "order_summary_product_name": "order-item-name",
                "order_summary_product_quantity": "order-item-quantity",
                "order_summary_product_price": "order-item-price",
                "subtotal_value": "subtotal-value",
                "shipping_value": "shipping-value",
                "total_value": "total-value"
            }
        }

    def assert_order_details_title(self):
        expect(self.page.get_by_test_id(self.locators["order_details_title"])).to_be_visible()

    def get_order_id(self):
        return self.page.get_by_test_id(self.locators["order_id"])

    def get_back_to_home_button(self):
        return self.page.get_by_test_id(self.locators["back_to_home_button"])

    def click_back_to_home_button(self):
        self.get_back_to_home_button().click()

    def assert_order_placed_name(self):
        expect(self.page.get_by_test_id(self.locators["order_placed_name"])).to_be_visible()

    def assert_order_placed_message(self):
        expect(self.page.get_by_test_id(self.locators["order_placed_message"])).to_be_visible()

    def assert_order_placed_date(self):
        expect(self.page.get_by_test_id(self.locators["order_placed_date"])).to_be_visible()

    def assert_order_information_title(self):
        expect(self.page.get_by_test_id(self.locators["order_information"]["order_information_title"])).to_be_visible()

    def assert_order_confirmed_title(self):
        expect(self.page.get_by_test_id(self.locators["order_information"]["order_confirmed_title"])).to_be_visible()

    def assert_order_confirmed_message(self):
        expect(self.page.get_by_test_id(self.locators["order_information"]["order_confirmed_message"])).to_be_visible()

    def assert_shipping_details_title(self):
        expect(self.page.get_by_test_id(self.locators["order_information"]["shipping_details_title"])).to_be_visible()

    def assert_shipping_email_value(self, email):
        expect(self.page.get_by_test_id(self.locators["order_information"]["shipping_email_value"])).to_contain_text(email)

    def assert_payment_method_amount(self, amount):
        expect(self.page.get_by_test_id(self.locators["order_information"]["payment_method_amount"])).to_contain_text(amount)

    def assert_delivery_address_label(self):
        expect(self.page.get_by_test_id(self.locators["order_information"]["delivery_address_label"])).to_be_visible()

    def assert_delivery_address_value(self):
        expect(self.page.get_by_test_id(self.locators["order_information"]["delivery_address_value"])).to_be_visible()

    def get_continue_shopping_button(self):
        return self.page.get_by_test_id(self.locators["order_information"]["continue_shopping_button"])

    def click_continue_shopping_button(self):
        self.get_continue_shopping_button().click()

    def assert_continue_shopping_button(self):
        expect(self.get_continue_shopping_button()).to_be_visible()

    def assert_order_summary_title(self):
        expect(self.page.get_by_test_id(self.locators["order_summary"]["order_summary_title"])).to_be_visible()

    def assert_order_summary_product_name(self, product_name):
        expect(self.page.get_by_test_id(self.locators["order_summary"]["order_summary_product_name"])).to_contain_text(product_name)

    def assert_order_summary_product_quantity(self, quantity):
        expect(self.page.get_by_test_id(self.locators["order_summary"]["order_summary_product_quantity"])).to_contain_text(quantity)

    def assert_order_summary_product_price(self, price):
        expect(self.page.get_by_test_id(self.locators["order_summary"]["order_summary_product_price"])).to_contain_text(price)

    def assert_order_summary_subtotal_value(self, subtotal):
        expect(self.page.get_by_test_id(self.locators["order_summary"]["subtotal_value"])).to_contain_text(subtotal)

    def assert_order_summary_shipping_value(self, shipping):
        expect(self.page.get_by_test_id(self.locators["order_summary"]["shipping_value"])).to_contain_text(shipping)

    def assert_order_summary_total_value(self, total):
        expect(self.page.get_by_test_id(self.locators["order_summary"]["total_value"])).to_contain_text(total)