import time
from playwrightTestingPractice.pageobjects.shoppingcart import Shoppingcart
from playwrightTestingPractice.pageobjects.checkout_information_order_confirmation_page import Orderpage
# from playwrightTestingPractice.Utilities.utility import user_credentials
# from playwrightTestingPractice.pageobjects.login import Login

def test_shoppingcart_page(browserInstance,common_steps):
    homepage_categories,count1=common_steps
    homepage_categories.cart_link()
    shop_obj=Shoppingcart(browserInstance)
    shop_obj.shopping()
    assert shop_obj.apply_coupon()=="Error: Coupon is either invalid, expired or reached it's usage limit!"
    assert "Success: Coupon has been removed" in shop_obj.remove_coupon()
    shop_obj.estimate_shipping()

def test_remove_product(browserInstance,common_steps):
    homepage_categories,count1=common_steps
    homepage_categories.cart_link()
    shop_obj=Shoppingcart(browserInstance)
    shop_obj.remove_product_from_cart()
def test_extract_cart_detail(browserInstance,common_steps):
    homepage_categories,count1=common_steps
    homepage_categories.cart_link()
    shop_obj=Shoppingcart(browserInstance)
    shop_obj.extract_shopping_cart_details()

def test_update_quantity(browserInstance,common_steps):
    homepage_categories,count1=common_steps
    homepage_categories.cart_link()
    shop_obj=Shoppingcart(browserInstance)
    total,calculate=shop_obj.update_quantity_calculate()
    assert calculate in total

def test_total_calculation(browserInstance,common_steps):
    homepage_categories,count1=common_steps
    homepage_categories.cart_link()
    shop_obj=Shoppingcart(browserInstance)
    uitotal,cal_total=shop_obj.consolidated_total()
    assert uitotal==cal_total

def test_orderconfirmation_page(browserInstance,common_steps):
    homepage_categories,count1=common_steps
    homepage_categories.cart_link()
    shop_obj=Shoppingcart(browserInstance)
    order_page=Orderpage(browserInstance)
    shop_obj.click_checkout()
    assert order_page.order_confirmation_page() == " Checkout Confirmation"
    time.sleep(3)

    

    


    