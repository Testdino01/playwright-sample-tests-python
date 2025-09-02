from .base_page import BasePage
from playwright.sync_api import expect

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locators = {
            "shipping_address": {
                "checkout_title": "checkout-title",
                "checkout_shipping_address_title": "checkout-shipping-address-title",
                "checkout_shipping_address_first_name": "checkout-first-name-input",
                "checkout_shipping_address_email": "checkout-email-input",
                "checkout_shipping_address_city": "checkout-city-input",
                "checkout_shipping_address_state": "checkout-state-input",
                "checkout_shipping_address_street_address": "checkout-street-input",
                "checkout_shipping_address_zip_code": "checkout-zip-code-input",
                "checkout_shipping_address_country": "checkout-country-input",
                "checkout_cancel_button": "checkout-cancel-button",
                "checkout_change_shipping_address_link": '[data-testid="checkout-change-address-button"]',
                "add_new_shipping_address_button": '[data-testid="add-new-address-button"]',
                "address_first_name": '[data-testid="checkout-first-name-input"]',
                "checkout_save_address_button": "checkout-save-address-button",
            },
            "payment_method": {
                "checkout_payment_method_title": "checkout-payment-method-title",
                "checkout_credit_card_button": "checkout-credit-card-button",
                "checkout_debit_card_button": "checkout-debit-card-button",
                "checkout_netbanking_button": "checkout-netbanking-button",
                "checkout_cod_button": "checkout-cod-button",
                "checkout_card_number_input": "checkout-card-number-input",
                "checkout_card_holder_name_input": "checkout-cardholder-name-input",
                "checkout_expiration_date_month_input": "checkout-expiration-date-month-input",
                "checkout_expiration_date_year_input": "checkout-expiration-date-year-input",
                "checkout_cvv_input": "checkout-cvv-input",
            },
            "order_summary": {
                "checkout_order_summary_title": "checkout-order-summary-title",
                "checkout_order_summary_image": '[data-testid="checkout-order-summary-title"] + div img',
                "checkout_product_name": "checkout-product-header",
                "checkout_product_quantity": "checkout-product-quantity",
                "checkout_product_price": "checkout-product-price",
                "checkout_subtotal_value": "checkout-subtotal-value",
                "checkout_shipping_value": "checkout-shipping-value",
                "checkout_total_value": "checkout-total-value",
                "checkout_place_order_button": "checkout-place-order-button",
                "checkout_continue_shopping_button": "checkout-continue-shopping-button"
            },
            "checkout_title": "h1[data-testid='checkout-title']",
            "product_name_in_checkout": "//h3[normalize-space()='{}']",
            "cash_on_delivery_button": "//button[normalize-space()='Cash on Delivery']",
            "cash_on_delivery_text": "//p[normalize-space()='Cash on Delivery']",
            "place_order_button": "//button[normalize-space()='Place Order']",
            "order_success_message": "//p[contains(text(), 'Your order was placed successf')]",
            "order_item_name_confirmation": "p[data-testid='order-item-name']",
            "continue_shopping_button": 'button[data-testid="continue-shopping-button"]',
            "order_confirmed_title": '[data-testid="order-confirmed-title"]'
        }

    # **************** Shipping Address **************** #
    def assert_checkout_title(self):
        expect(self.page.get_by_test_id(self.locators["shipping_address"]["checkout_title"])).to_be_visible(timeout=10000)

    def get_shipping_address_title(self):
        return self.page.get_by_test_id(self.locators["shipping_address"]["checkout_shipping_address_title"])

    def get_shipping_address_first_name(self):
        return self.page.get_by_test_id(self.locators["shipping_address"]["checkout_shipping_address_first_name"])

    def get_shipping_address_email(self):
        return self.page.get_by_test_id(self.locators["shipping_address"]["checkout_shipping_address_email"])

    def get_shipping_address_city(self):
        return self.page.get_by_test_id(self.locators["shipping_address"]["checkout_shipping_address_city"])

    def get_shipping_address_state(self):
        return self.page.get_by_test_id(self.locators["shipping_address"]["checkout_shipping_address_state"])

    def get_shipping_address_street_address(self):
        return self.page.get_by_test_id(self.locators["shipping_address"]["checkout_shipping_address_street_address"])

    def get_shipping_address_zip_code(self):
        return self.page.get_by_test_id(self.locators["shipping_address"]["checkout_shipping_address_zip_code"])

    def get_shipping_address_country(self):
        return self.page.get_by_test_id(self.locators["shipping_address"]["checkout_shipping_address_country"])

    def get_shipping_address_cancel_button(self):
        return self.page.get_by_test_id(self.locators["shipping_address"]["checkout_cancel_button"])

    def click_cancel_button(self):
        self.get_shipping_address_cancel_button().click()

    def get_save_address_button(self):
        return self.page.get_by_test_id(self.locators["shipping_address"]["checkout_save_address_button"])

    def click_save_address_button(self):
        self.get_save_address_button().click()

    def fill_shipping_address(self, first_name, email, city, state, street_address, zip_code, country):
        self.get_shipping_address_first_name().fill(first_name)
        self.get_shipping_address_email().fill(email)
        self.get_shipping_address_city().fill(city)
        self.get_shipping_address_state().fill(state)
        self.get_shipping_address_street_address().fill(street_address)
        self.get_shipping_address_zip_code().fill(zip_code)
        self.get_shipping_address_country().fill(country)

    def get_shipping_address_change_link(self):
        return self.page.locator(self.locators["shipping_address"]["checkout_change_shipping_address_link"])

    def click_change_shipping_address_link(self):
        self.get_shipping_address_change_link().click(force=True)

    def get_add_new_shipping_address_button(self):
        return self.page.locator(self.locators["shipping_address"]["add_new_shipping_address_button"])

    def click_add_new_shipping_address_button(self):
        self.get_add_new_shipping_address_button().click(force=True)

    def assert_address_added_toast(self):
        expect(self.page.get_by_text('Address added successfully')).to_be_visible(timeout=10000)

    # **************** Payment Method **************** #
    def get_address_first_name(self):
        return self.page.locator(self.locators["shipping_address"]["address_first_name"])

    def get_payment_method_title(self):
        return self.page.get_by_test_id(self.locators["payment_method"]["checkout_payment_method_title"])

    def get_credit_card_button(self):
        return self.page.get_by_test_id(self.locators["payment_method"]["checkout_credit_card_button"])

    def get_debit_card_button(self):
        return self.page.get_by_test_id(self.locators["payment_method"]["checkout_debit_card_button"])

    def get_netbanking_button(self):
        return self.page.get_by_test_id(self.locators["payment_method"]["checkout_netbanking_button"])

    def get_cod_button(self):
        return self.page.get_by_test_id(self.locators["payment_method"]["checkout_cod_button"])

    def click_cod_button(self):
        self.get_cod_button().click()

    def get_card_number_input(self):
        return self.page.get_by_test_id(self.locators["payment_method"]["checkout_card_number_input"])

    def get_card_holder_name_input(self):
        return self.page.get_by_test_id(self.locators["payment_method"]["checkout_card_holder_name_input"])

    def get_expiration_date_month_input(self):
        return self.page.get_by_test_id(self.locators["payment_method"]["checkout_expiration_date_month_input"])

    def get_expiration_date_year_input(self):
        return self.page.get_by_test_id(self.locators["payment_method"]["checkout_expiration_date_year_input"])

    def get_cvv_input(self):
        return self.page.get_by_test_id(self.locators["payment_method"]["checkout_cvv_input"])

    # ************************** Order Summary ************************** #
    def get_order_summary_title(self):
        return self.page.get_by_test_id(self.locators["order_summary"]["checkout_order_summary_title"])

    def assert_order_summary_title(self):
        expect(self.page.get_by_test_id(self.locators["order_summary"]["checkout_order_summary_title"])).to_be_visible()

    def get_order_summary_image(self):
        return self.page.locator(self.locators["order_summary"]["checkout_order_summary_image"])

    def get_order_summary_product_name(self):
        return self.page.get_by_test_id(self.locators["order_summary"]["checkout_product_name"])

    def get_order_summary_product_quantity(self):
        return self.page.get_by_test_id(self.locators["order_summary"]["checkout_product_quantity"])

    def get_order_summary_product_price(self):
        return self.page.get_by_test_id(self.locators["order_summary"]["checkout_product_price"])

    def get_order_summary_subtotal_value(self):
        return self.page.get_by_test_id(self.locators["order_summary"]["checkout_subtotal_value"]).text_content()

    def get_order_summary_shipping_value(self):
        return self.page.get_by_test_id(self.locators["order_summary"]["checkout_shipping_value"])

    def get_order_summary_total_value(self):
        return self.page.get_by_test_id(self.locators["order_summary"]["checkout_total_value"])

    def get_place_order_button(self):
        return self.page.get_by_test_id(self.locators["order_summary"]["checkout_place_order_button"])

    def click_place_order_button(self):
        self.get_place_order_button().click()

    def get_continue_shopping_button(self):
        return self.page.get_by_test_id(self.locators["order_summary"]["checkout_continue_shopping_button"])

    def click_continue_shopping_button(self):
        self.get_continue_shopping_button().click()

    def verify_checkout_title(self):
        expect(self.page.locator(self.locators["checkout_title"])).to_be_visible()

    def verify_product_in_checkout(self, product_name):
        locator = self.page.locator(self.locators["product_name_in_checkout"].format(product_name)).nth(1)
        expect(locator).to_be_visible()
        expect(locator).to_have_text(product_name)

    def select_cash_on_delivery(self):
        self.page.locator(self.locators["cash_on_delivery_button"]).click(force=True)

    def verify_cash_on_delivery_selected(self):
        expect(self.page.locator(self.locators["cash_on_delivery_text"])).to_be_visible()

    def click_on_place_order(self):
        self.page.locator(self.locators["place_order_button"]).click(force=True)

    def verify_order_placed_successfully(self):
        expect(self.page.locator(self.locators["order_success_message"])).to_be_visible()

    def verify_order_item_name(self, product_name):
        expect(self.page.locator(self.locators["order_item_name_confirmation"])).to_be_visible()
        expect(self.page.locator(self.locators["order_item_name_confirmation"])).to_have_text(product_name)

    def verify_order_confirmed_title(self):
        expect(self.page.locator(self.locators["order_confirmed_title"])).to_be_visible(timeout=50000)

    def get_on_continue_shopping_button(self):
        return self.page.locator(self.locators["continue_shopping_button"])

    def click_on_continue_shopping_button(self):
        self.get_on_continue_shopping_button().click(timeout=50000)