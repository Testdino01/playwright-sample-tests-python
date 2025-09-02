from .login_page import LoginPage
from .inventory_page import InventoryPage
from .signup_page import SignupPage
from .home_page import HomePage
from .all_products_page import AllProductsPage
from .product_details_page import ProductDetailsPage
from .cart_page import CartPage
from .checkout_page import CheckoutPage
from .order_page import OrderPage
from .user_page import UserPage
from .order_details_page import OrderDetailsPage
from .contact_us_page import ContactUsPage

class AllPages:
    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.signup_page = SignupPage(page)
        self.home_page = HomePage(page)
        self.all_products_page = AllProductsPage(page)
        self.product_details_page = ProductDetailsPage(page)
        self.cart_page = CartPage(page)
        self.checkout_page = CheckoutPage(page)
        self.order_page = OrderPage(page)
        self.user_page = UserPage(page)
        self.order_details_page = OrderDetailsPage(page)
        self.contact_us_page = ContactUsPage(page)