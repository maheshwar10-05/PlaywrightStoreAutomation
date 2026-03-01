import pytest
from playwrightTestingPractice.pages.shoppingcart import Shoppingcart
from playwrightTestingPractice.pages.checkout_information_order_confirmation_page import Orderpage


async def test_shoppingcart_page(browserInstance, home_fixture):
    # Await the navigation link
    await home_fixture.cart_link()
    
    # Initialize Page Object with the async browserInstance
    shop_obj = Shoppingcart(browserInstance)
    
    # Rule: Always await methods that perform actions or return data
    await shop_obj.shopping()
    
    # Use await inside assertions
    coupon_msg = await shop_obj.apply_coupon()
    assert coupon_msg == "Error: Coupon is either invalid, expired or reached it's usage limit!"
    
    remove_msg = await shop_obj.remove_coupon()
    assert "Success: Coupon has been removed" in remove_msg
    
    await shop_obj.estimate_shipping()


async def test_remove_product(browserInstance, home_fixture):
    await home_fixture.cart_link()
    shop_obj = Shoppingcart(browserInstance)
    await shop_obj.remove_product_from_cart()


async def test_extract_cart_detail(browserInstance, home_fixture):
    await home_fixture.cart_link()
    shop_obj = Shoppingcart(browserInstance)
    await shop_obj.extract_shopping_cart_details()


async def test_update_quantity(browserInstance, home_fixture):
    await home_fixture.cart_link()
    shop_obj = Shoppingcart(browserInstance)
    
    # Await the tuple unpacking
    total, calculate = await shop_obj.update_quantity_calculate()
    assert calculate in total


async def test_total_calculation(browserInstance, home_fixture):
    await home_fixture.cart_link()
    shop_obj = Shoppingcart(browserInstance)
    
    uitotal, cal_total = await shop_obj.consolidated_total()
    assert cal_total in uitotal

@pytest.mark.no_auth
async def test_orderconfirmation_page(browserInstance, home_fixture):
    await home_fixture.cart_link()
    shop_obj = Shoppingcart(browserInstance)
    order_page = Orderpage(browserInstance)
    
    await shop_obj.click_checkout()
    
    # Await the final page validation
    confirmation_text = await order_page.order_confirmation_page()
    assert confirmation_text == " Checkout Confirmation"