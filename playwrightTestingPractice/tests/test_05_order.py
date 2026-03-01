import pytest
# time import removed as it is usually redundant in Playwright Async
from playwrightTestingPractice.pages.checkout_information_order_confirmation_page import Orderpage
from playwrightTestingPractice.pages.shoppingcart import Shoppingcart
from playwrightTestingPractice.pages.orderhistory import Orderhistory
from playwrightTestingPractice.pages.logout_orderdetails_entry import EnterOrder

#
async def test_pop(browserInstance, home_fixture):
    pop_up = Orderpage(browserInstance)
    shop_obj = Shoppingcart(browserInstance)
    
    await home_fixture.cart_link()
    await shop_obj.click_checkout()
    await pop_up.return_policy_popup()
    await pop_up.pop_up_text()

#
async def test_delivery_payment_information(browserInstance, home_fixture):
    pop_up = Orderpage(browserInstance)
    shop_obj = Shoppingcart(browserInstance)
    
    await home_fixture.cart_link()
    await shop_obj.click_checkout()
    
    # Await methods within assertions
    assert await pop_up.edit_shipping() == " Delivery Information"
    assert await pop_up.edit_payment() == " Payment Information"
    assert await pop_up.edit_cart() == " Shopping Cart"

#
async def test_order_confirmation(browserInstance, home_fixture):
    pop_up = Orderpage(browserInstance)
    
    await home_fixture.checkout_click()
    # Capturing the result of the async method first for cleaner assertions
    confirm_result = await pop_up.click_confirm_order()
    assert 'Processed' in confirm_result

    order_id_result = await pop_up.order_id()
    assert "Contact" in order_id_result

#
async def test_order_history(browserInstance, home_fixture):
    pop_up = Orderpage(browserInstance)
    orderobj = Orderhistory(page=browserInstance)
    
    await home_fixture.profile_tab_links()
    target_page = await orderobj.validate_excel_data()
    assert "Order" in target_page

#
async def test_excel(browserInstance, home_fixture):
    orderobj = Orderhistory(page=browserInstance)
    await home_fixture.profile_tab_links()
    await orderobj.excel_products_quantity_view()

#
async def test_export_order_excel(browserInstance, home_fixture):
    orderobj = Orderhistory(page=browserInstance)
    await home_fixture.profile_tab_links()
    await orderobj.export_total_excel()

#
async def test_date_added_excel(browserInstance, home_fixture):
    orderobj = Orderhistory(page=browserInstance)
    await home_fixture.profile_tab_links()
    await orderobj.date_export_excel()

#
async def test_status_info(browserInstance, home_fixture):
    orderobj = Orderhistory(page=browserInstance)
    await home_fixture.profile_tab_links()
    await orderobj.status_excel()

#
async def test_click_back(browserInstance, home_fixture):
    pop_up = Orderpage(browserInstance)
    await home_fixture.cart_link()
    await home_fixture.checkout_click()
    await pop_up.click_back()

# Example of how the commented out test would look:
# #
# async def test_logout_orderdetail(browserInstance, home_fixture):
#     await test_account_link(browserInstance, home_fixture)
#     import_order = EnterOrder(browserInstance)
#     await import_order.order_input()