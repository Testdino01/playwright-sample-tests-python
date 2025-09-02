import os
import pytest
from dotenv import load_dotenv
load_dotenv()
from playwright.sync_api import Page, expect
from pages.all_pages import AllPages

@pytest.fixture(autouse=True)
def setup(page: Page):
    global all_pages
    all_pages = AllPages(page)
    page.goto('/')

def login(username=None, password=None):
    username = username or os.getenv("USERNAME")
    password = password or os.getenv("PASSWORD")
    if not username or not password:
        raise ValueError("USERNAME and PASSWORD environment variables must be set.")
    all_pages.login_page.click_on_user_profile_icon()
    all_pages.login_page.validate_sign_in_page()
    all_pages.login_page.login(username, password)

def login1(username=None, password=None):
    username = username or os.getenv("USERNAME1")
    password = password or os.getenv("PASSWORD")
    if not username or not password:
        raise ValueError("USERNAME1 and PASSWORD environment variables must be set.")
    all_pages.login_page.click_on_user_profile_icon()
    all_pages.login_page.validate_sign_in_page()
    all_pages.login_page.login(username, password)

def logout():
    all_pages.login_page.click_on_user_profile_icon()
    all_pages.login_page.click_on_logout_button()

def test_user_can_login_and_logout(page: Page):
    login()
    logout()

def test_user_can_update_personal_information(page: Page):
    login()
    all_pages.user_page.click_on_user_profile_icon()
    all_pages.user_page.update_personal_info()
    all_pages.user_page.verify_personal_info_updated()

def test_user_can_add_edit_delete_addresses(page: Page):
    login()
    # Add address
    all_pages.user_page.click_on_user_profile_icon()
    all_pages.user_page.click_on_address_tab()
    all_pages.user_page.click_on_add_address_button()
    all_pages.user_page.fill_address_form()
    all_pages.user_page.verify_the_address_is_added()
    # Edit address
    all_pages.user_page.click_on_edit_address_button()
    all_pages.user_page.update_address_form()
    all_pages.user_page.verify_the_updated_address_is_added()
    # Delete address
    all_pages.user_page.click_on_delete_address_button()

def test_user_can_change_password(page: Page):
    login1()
    all_pages.user_page.click_on_user_profile_icon()
    all_pages.user_page.click_on_security_button()
    all_pages.user_page.enter_new_password()
    all_pages.user_page.enter_confirm_new_password()
    all_pages.user_page.click_on_update_password_button()
    all_pages.user_page.get_update_password_notification()
    logout()
    all_pages.login_page.login(os.getenv("USERNAME1"), os.getenv("NEW_PASSWORD"))
    all_pages.user_page.click_on_user_profile_icon()
    all_pages.user_page.click_on_security_button()
    all_pages.user_page.revert_password_back_to_original()
    all_pages.user_page.get_update_password_notification()

def test_new_user_can_add_addresses(page: Page):
    login()
    all_pages.user_page.click_on_user_profile_icon()
    all_pages.user_page.click_on_address_tab()
    all_pages.user_page.click_on_add_address_button()
    all_pages.user_page.check_add_new_address_menu()
    all_pages.user_page.fill_address_form()

def test_user_can_complete_order_journey(page: Page):
    product_name = 'GoPro HERO10 Black'
    login()
    all_pages.inventory_page.click_on_shop_now_button()
    all_pages.inventory_page.click_on_all_products_link()
    all_pages.inventory_page.search_product(product_name)
    all_pages.inventory_page.verify_product_title_visible(product_name)
    all_pages.inventory_page.click_on_add_to_cart_icon()
    all_pages.cart_page.click_on_cart_icon()
    all_pages.cart_page.verify_cart_item_visible(product_name)
    all_pages.cart_page.click_on_checkout_button()
    all_pages.checkout_page.verify_product_in_checkout(product_name)
    all_pages.checkout_page.select_cash_on_delivery()
    all_pages.checkout_page.verify_cash_on_delivery_selected()
    all_pages.checkout_page.click_on_place_order()
    all_pages.checkout_page.verify_order_placed_successfully()

def test_user_can_place_and_cancel_order(page: Page):
    product_name = 'GoPro HERO10 Black'
    product_price_and_quantity = '₹49,999 × 1'
    product_quantity = '1'
    order_status_processing = 'Processing'
    order_status_canceled = 'Canceled'
    login()
    all_pages.inventory_page.click_on_all_products_link()
    all_pages.inventory_page.search_product(product_name)
    all_pages.inventory_page.verify_product_title_visible(product_name)
    all_pages.inventory_page.click_on_add_to_cart_icon()
    all_pages.cart_page.click_on_cart_icon()
    all_pages.cart_page.verify_cart_item_visible(product_name)
    all_pages.cart_page.click_on_checkout_button()
    all_pages.checkout_page.verify_checkout_title()
    all_pages.checkout_page.verify_product_in_checkout(product_name)
    all_pages.checkout_page.select_cash_on_delivery()
    all_pages.checkout_page.verify_cash_on_delivery_selected()
    all_pages.checkout_page.click_on_place_order()
    all_pages.checkout_page.verify_order_placed_successfully()
    all_pages.checkout_page.verify_order_item_name(product_name)
    all_pages.inventory_page.click_on_continue_shopping()
    all_pages.login_page.click_on_user_profile_icon()
    all_pages.order_page.click_on_my_orders_tab()
    # all_pages.order_page.verify_my_orders_title()
    all_pages.order_page.click_on_pagination_button(2)
    all_pages.order_page.verify_product_in_order_list(product_name)
    all_pages.order_page.verify_price_and_quantity_in_order_list(product_price_and_quantity)
    all_pages.order_page.verify_order_status_in_list(order_status_processing, product_name)
    all_pages.order_page.click_on_pagination_button(1)
    all_pages.order_page.click_view_details_button(1)
    all_pages.order_page.verify_order_details_title()
    all_pages.order_page.verify_order_summary(product_name, product_quantity, '₹49,999', order_status_processing)
    all_pages.order_page.click_cancel_order_button(2)
    all_pages.order_page.confirm_cancellation()
    all_pages.order_page.verify_cancellation_confirmation_message()
    all_pages.order_page.verify_my_orders_count()
    all_pages.order_page.click_on_my_orders_tab()
    all_pages.order_page.verify_my_orders_title()
    all_pages.order_page.click_on_pagination_button(2)
    all_pages.order_page.verify_order_status_in_list(order_status_canceled, product_name)

def test_new_user_registration_to_order(page: Page):
    email = f"test+{int(os.times()[4])}@test.com"
    first_name = 'Test'
    last_name = 'User'
    login_page = all_pages.login_page
    signup_page = all_pages.signup_page
    home_page = all_pages.home_page
    all_products_page = all_pages.all_products_page
    product_details_page = all_pages.product_details_page
    cart_page = all_pages.cart_page
    checkout_page = all_pages.checkout_page
    order_details_page = all_pages.order_details_page

    # Register
    login_page.click_on_user_profile_icon()
    login_page.validate_sign_in_page()
    login_page.click_on_signup_link()
    signup_page.assert_signup_page()
    signup_page.signup(first_name, last_name, email, os.getenv("PASSWORD"))
    signup_page.verify_success_sign_up()
    # Login
    login_page.validate_sign_in_page()
    login_page.login(email, os.getenv("PASSWORD"))
    login_page.verify_success_sign_in()
    expect(home_page.get_home_nav()).to_be_visible(timeout=30000)
    # Add to wishlist, view product
    home_page.click_all_products_nav()
    all_products_page.assert_all_products_title()
    product_name = all_products_page.get_nth_product_name(1)
    product_price = all_products_page.get_nth_product_price(1)
    product_review_count = all_products_page.get_nth_product_review_count(1)
    all_products_page.click_nth_product_wishlist_icon(1)
    expect(all_products_page.get_nth_product_wishlist_icon_count(1)).to_contain_text('1')
    all_products_page.click_nth_product(1)
    product_details_page.assert_product_name_title(product_name)
    product_details_page.assert_product_price(product_name, product_price)
    product_details_page.assert_product_review_count(product_name, product_review_count)
    expect(all_products_page.get_nth_product_wishlist_icon_count(1)).to_contain_text('1')

    product_details_page.click_add_to_cart_button()
    product_details_page.click_cart_icon()
    cart_page.assert_your_cart_title()
    expect(cart_page.get_cart_item_name()).to_contain_text(product_name, timeout=10000)
    expect(cart_page.get_cart_item_price()).to_contain_text(product_price)
    expect(cart_page.get_cart_item_quantity()).to_contain_text('1')
    cart_page.click_increase_quantity_button()
    expect(cart_page.get_cart_item_quantity()).to_contain_text('2')
    clean_price = product_price.replace('₹', '').replace(',', '')
    price_value = float(clean_price) * 2
    expect(cart_page.get_total_value()).to_contain_text(f"{price_value:,.0f}")
    cart_page.click_on_checkout_button()
    checkout_page.verify_checkout_title()
    checkout_page.fill_shipping_address(first_name, email, 'New York', 'New York', '123 Main St', '10001', 'United States')
    checkout_page.click_save_address_button()
    checkout_page.assert_address_added_toast()
    checkout_page.select_cash_on_delivery()
    checkout_page.verify_checkout_title()
    checkout_page.assert_order_summary_title()
    expect(checkout_page.get_order_summary_image()).to_be_visible()
    expect(checkout_page.get_order_summary_product_name()).to_contain_text(product_name)
    checkout_page.verify_product_in_checkout(product_name)
    expect(checkout_page.get_order_summary_product_quantity()).to_contain_text('2')
    expect(checkout_page.get_order_summary_product_price()).to_contain_text(product_price)
    subtotal_value = float(clean_price) * 2
    formatted_subtotal = f"{subtotal_value:,.0f}"
    # expect(checkout_page.get_order_summary_subtotal_value()).to_contain(formatted_subtotal)
    expect(checkout_page.get_order_summary_shipping_value()).to_contain_text('Free')
    checkout_page.click_on_place_order()
    order_details_page.assert_order_details_title()
    order_details_page.assert_order_placed_name()
    order_details_page.assert_order_placed_message()
    order_details_page.assert_order_placed_date()
    order_details_page.assert_order_information_title()
    order_details_page.assert_order_confirmed_title()
    order_details_page.assert_order_confirmed_message()
    order_details_page.assert_shipping_details_title()
    order_details_page.assert_shipping_email_value(email)
    order_details_page.assert_payment_method_amount(formatted_subtotal)
    order_details_page.assert_delivery_address_label()
    order_details_page.assert_delivery_address_value()
    order_details_page.assert_continue_shopping_button()
    order_details_page.assert_order_summary_title()
    order_details_page.assert_order_summary_product_name(product_name)
    order_details_page.assert_order_summary_product_quantity('2')
    order_details_page.assert_order_summary_product_price(product_price)
    order_details_page.assert_order_summary_subtotal_value(formatted_subtotal)
    order_details_page.assert_order_summary_shipping_value('Free')
    order_details_page.assert_order_summary_total_value(formatted_subtotal)
    order_details_page.click_back_to_home_button()

def test_add_product_to_cart_before_login_then_complete_order(page: Page):
    all_pages.home_page.click_on_shop_now_button()
    all_pages.home_page.click_product_image()
    all_pages.home_page.click_add_to_cart_button()
    all_pages.home_page.validate_add_cart_notification()
    all_pages.login_page.click_on_user_profile_icon()

    # Step: Login and complete order
    login()
    all_pages.cart_page.click_on_cart_icon()
    all_pages.cart_page.click_on_checkout_button()
    all_pages.checkout_page.verify_checkout_title()
    all_pages.checkout_page.select_cash_on_delivery()
    all_pages.checkout_page.verify_cash_on_delivery_selected()
    all_pages.checkout_page.click_on_place_order()
    all_pages.checkout_page.verify_order_placed_successfully()

def test_filter_products_by_price_range(page: Page):
    login()
    all_pages.home_page.click_on_shop_now_button()
    all_pages.home_page.click_on_filter_button()
    all_pages.home_page.adjust_price_range_slider('10000', '20000')
    all_pages.home_page.click_on_filter_button()

def test_add_product_to_wishlist_move_to_cart_and_checkout(page: Page):
    login()
    # Step: Add product to wishlist and then add to cart
    all_pages.home_page.click_on_shop_now_button()
    all_pages.inventory_page.add_to_wishlist()
    all_pages.inventory_page.assert_wishlist_icon()
    all_pages.inventory_page.click_on_wishlist_icon_header()
    all_pages.inventory_page.assert_wishlist_page()
    all_pages.inventory_page.click_on_wishlist_add_to_card()

    # Step: Checkout product added to cart
    all_pages.cart_page.click_on_cart_icon()
    all_pages.cart_page.click_on_checkout_button()
    all_pages.checkout_page.verify_checkout_title()
    all_pages.checkout_page.select_cash_on_delivery()
    all_pages.checkout_page.verify_cash_on_delivery_selected()
    all_pages.checkout_page.click_on_place_order()
    all_pages.checkout_page.verify_order_placed_successfully()

def test_new_user_views_and_cancels_order(page: Page):
    email = f"test+{int(os.times()[4])}@test.com"
    first_name = 'Test'
    last_name = 'User'
    product_name = "Rode NT1-A Condenser Mic"

    # Step: Register
    all_pages.login_page.click_on_user_profile_icon()
    all_pages.login_page.validate_sign_in_page()
    all_pages.login_page.click_on_signup_link()
    all_pages.signup_page.assert_signup_page()
    all_pages.signup_page.signup(first_name, last_name, email, os.getenv("PASSWORD"))
    all_pages.signup_page.verify_success_sign_up()

    # Step: Login
    all_pages.login_page.validate_sign_in_page()
    all_pages.login_page.login(email, os.getenv("PASSWORD"))
    all_pages.login_page.verify_success_sign_in()
    expect(all_pages.home_page.get_home_nav()).to_be_visible(timeout=30000)

    # Step: Navigate to All Products and view details of a random product
    all_pages.home_page.click_all_products_nav()
    all_pages.all_products_page.assert_all_products_title()
    product_name = all_pages.all_products_page.get_nth_product_name(1)
    all_pages.all_products_page.click_nth_product(1)
    all_pages.product_details_page.click_add_to_cart_button()

    # Step: Add product to cart, add new address and checkout
    all_pages.product_details_page.click_cart_icon()
    all_pages.cart_page.assert_your_cart_title()
    expect(all_pages.cart_page.get_cart_item_name()).to_contain_text(product_name, timeout=10000)
    all_pages.cart_page.click_on_checkout_button()
    all_pages.checkout_page.verify_checkout_title()
    all_pages.checkout_page.fill_shipping_address(
        first_name, email, 'New York', 'New York', '123 Main St', '10001', 'United States'
    )
    all_pages.checkout_page.click_save_address_button()
    all_pages.checkout_page.assert_address_added_toast()

    # Step: Complete order and verify in my orders
    all_pages.checkout_page.select_cash_on_delivery()
    all_pages.checkout_page.verify_checkout_title()
    all_pages.checkout_page.click_on_place_order()
    all_pages.checkout_page.verify_order_placed_successfully()
    all_pages.inventory_page.click_on_continue_shopping()
    all_pages.login_page.click_on_user_profile_icon()
    all_pages.order_page.click_on_my_orders_tab()
    all_pages.order_page.click_cancel_order_button()
    all_pages.order_page.confirm_cancellation()

def test_new_user_registration_to_multiple_order_placement(page: Page):
    email = f"test+{int(os.times()[4])}@test.com"
    first_name = 'Test'
    last_name = 'User'
    product_name = "Rode NT1-A Condenser Mic"

    # Step: Register
    all_pages.login_page.click_on_user_profile_icon()
    all_pages.login_page.validate_sign_in_page()
    all_pages.login_page.click_on_signup_link()
    all_pages.signup_page.assert_signup_page()
    all_pages.signup_page.signup(first_name, last_name, email, os.getenv("PASSWORD"))
    all_pages.signup_page.verify_success_sign_up()

    # Step: Login
    all_pages.login_page.validate_sign_in_page()
    all_pages.login_page.login(email, os.getenv("PASSWORD"))
    all_pages.login_page.verify_success_sign_in()
    expect(all_pages.home_page.get_home_nav()).to_be_visible(timeout=30000)

    # Step: Navigate to All Products and view details of a random product
    all_pages.home_page.click_on_shop_now_button()
    all_pages.all_products_page.assert_all_products_title()
    all_pages.all_products_page.click_nth_product(1)
    all_pages.product_details_page.click_on_reviews_tab()
    all_pages.product_details_page.assert_reviews_tab()
    all_pages.product_details_page.click_on_additional_info_tab()
    all_pages.product_details_page.assert_additional_info_tab()

    # Step: Add product to cart, change quantity, add new address and checkout
    all_pages.product_details_page.click_add_to_cart_button()
    all_pages.product_details_page.click_cart_icon()
    all_pages.cart_page.click_increase_quantity_button()
    all_pages.cart_page.click_on_checkout_button()
    all_pages.checkout_page.verify_checkout_title()
    all_pages.checkout_page.select_cash_on_delivery()
    all_pages.checkout_page.verify_cash_on_delivery_selected()
    all_pages.checkout_page.fill_shipping_address(
        os.getenv("SFIRST_NAME"), email, os.getenv("SCITY"), os.getenv("SSTATE"),
        os.getenv("SSTREET_ADD"), os.getenv("SZIP_CODE"), os.getenv("SCOUNTRY")
    )
    all_pages.checkout_page.click_save_address_button()
    all_pages.checkout_page.click_on_place_order()
    all_pages.checkout_page.verify_order_placed_successfully()
    all_pages.checkout_page.verify_order_confirmed_title()
    all_pages.checkout_page.click_on_continue_shopping_button()

    # Step: Add another product to cart, select existing address and checkout
    all_pages.home_page.click_on_shop_now_button()
    all_pages.all_products_page.assert_all_products_title()
    all_pages.all_products_page.click_nth_product(1)
    all_pages.product_details_page.click_add_to_cart_button()
    all_pages.product_details_page.click_cart_icon()
    all_pages.cart_page.click_on_checkout_button()
    all_pages.checkout_page.verify_checkout_title()
    all_pages.checkout_page.select_cash_on_delivery()
    all_pages.checkout_page.verify_cash_on_delivery_selected()
    all_pages.checkout_page.click_on_place_order()
    all_pages.checkout_page.verify_order_placed_successfully()

def test_new_user_signup_login_and_navigate_home(page: Page):
    email = f"test+{int(os.times()[4])}@test.com"
    first_name = 'Test'
    last_name = 'User'

    # Step: Register
    all_pages.login_page.click_on_user_profile_icon()
    all_pages.login_page.validate_sign_in_page()
    all_pages.login_page.click_on_signup_link()
    all_pages.signup_page.assert_signup_page()
    all_pages.signup_page.signup(first_name, last_name, email, os.getenv("PASSWORD"))
    all_pages.signup_page.verify_success_sign_up()

    # Step: Login
    all_pages.login_page.validate_sign_in_page()
    all_pages.login_page.login(email, os.getenv("PASSWORD"))
    all_pages.login_page.verify_success_sign_in()
    expect(all_pages.home_page.get_home_nav()).to_be_visible(timeout=30000)

def test_fill_contact_us_page(page: Page):
    login()
    all_pages.home_page.click_on_contact_us_link()
    all_pages.contact_us_page.assert_contact_us_title()
    all_pages.contact_us_page.fill_contact_us_form()
    # all_pages.contact_us_page.verify_success_contact_us_form_submission()

def test_submit_product_review(page: Page):
    login()
    all_pages.home_page.click_on_shop_now_button()
    all_pages.all_products_page.assert_all_products_title()
    all_pages.all_products_page.click_nth_product(1)

    # Step: Submit a product review and verify submission
    all_pages.product_details_page.click_on_reviews_tab()
    all_pages.product_details_page.assert_reviews_tab()
    all_pages.product_details_page.click_on_write_a_review_btn()
    all_pages.product_details_page.fill_review_form()
    all_pages.product_details_page.assert_submitted_review({
        "name": "John Doe",
        "title": "Great Product",
        "opinion": "This product exceeded my expectations. Highly recommend!"
    })

def test_edit_and_delete_product_review(page: Page):
    # Step: Login and navigate to a product
    login()
    all_pages.home_page.click_on_shop_now_button()
    all_pages.all_products_page.assert_all_products_title()
    all_pages.all_products_page.click_nth_product(1)

    all_pages.product_details_page.click_on_reviews_tab()
    all_pages.product_details_page.assert_reviews_tab()
    all_pages.product_details_page.click_on_write_a_review_btn()
    all_pages.product_details_page.fill_review_form()
    all_pages.product_details_page.assert_submitted_review({
        "name": "John Doe",
        "title": "Great Product",
        "opinion": "This product exceeded my expectations. Highly recommend!"
    })

    all_pages.product_details_page.click_on_edit_review_btn()
    all_pages.product_details_page.update_review_form()
    all_pages.product_details_page.assert_updated_review({
        "title": "Updated Review Title",
        "opinion": "This is an updated review opinion."
    })

    all_pages.product_details_page.click_on_delete_review_btn()

def test_purchase_multiple_quantities_in_single_order(page: Page):
    product_name = "GoPro HERO10 Black"
    login()
    all_pages.inventory_page.click_on_shop_now_button()
    all_pages.inventory_page.click_on_all_products_link()
    all_pages.inventory_page.search_product(product_name)
    all_pages.inventory_page.verify_product_title_visible(product_name)
    all_pages.inventory_page.click_on_add_to_cart_icon()
    all_pages.cart_page.click_on_cart_icon()
    all_pages.cart_page.verify_cart_item_visible(product_name)
    all_pages.cart_page.click_increase_quantity_button()
    all_pages.cart_page.verify_increased_quantity('2')
    all_pages.cart_page.click_on_checkout_button()
    all_pages.checkout_page.verify_checkout_title()
    all_pages.checkout_page.verify_product_in_checkout(product_name)
    all_pages.checkout_page.select_cash_on_delivery()
    all_pages.checkout_page.verify_cash_on_delivery_selected()
    all_pages.checkout_page.click_on_place_order()
    all_pages.checkout_page.verify_order_placed_successfully()

def test_navbar_working_properly(page: Page):
    login()
    all_pages.home_page.click_back_to_home_button()
    # all_pages.home_page.assert_home_page()
    all_pages.home_page.click_all_products_nav()
    all_pages.all_products_page.assert_all_products_title()
    all_pages.home_page.click_on_contact_us_link()
    all_pages.contact_us_page.assert_contact_us_title()
    all_pages.home_page.click_about_us_nav()
    all_pages.home_page.assert_about_us_title()

def test_delete_selected_product_from_cart(page: Page):
    product_name = "GoPro HERO10 Black"
    login()
    all_pages.inventory_page.click_on_shop_now_button()
    all_pages.inventory_page.click_on_all_products_link()
    all_pages.inventory_page.search_product(product_name)
    all_pages.inventory_page.verify_product_title_visible(product_name)
    all_pages.inventory_page.click_on_add_to_cart_icon()
    all_pages.cart_page.click_on_cart_icon()
    all_pages.cart_page.verify_cart_item_visible(product_name)
    all_pages.cart_page.click_on_delete_product_icon()
    all_pages.cart_page.verify_cart_item_deleted(product_name)
    all_pages.cart_page.verify_empty_cart_message()
    all_pages.cart_page.click_on_start_shopping_button()
    all_pages.all_products_page.assert_all_products_title()