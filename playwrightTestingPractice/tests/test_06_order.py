import time,pytest
from playwrightTestingPractice.utils.utility import user_credentials,user_login
from playwrightTestingPractice.pages.checkout_information_order_confirmation_page import Orderpage
from playwrightTestingPractice.pages.shoppingcart import Shoppingcart
from playwrightTestingPractice.pages.orderhistory import Orderhistory
from playwrightTestingPractice.pages.logout_orderdetails_entry import EnterOrder
# from playwrightTestingPractice.tests.test_03_home_validation import test_account_link

def test_pop(browserInstance,home_fixture):

    pop_up=Orderpage(browserInstance)
    home_fixture.cart_link()
    shop_obj=Shoppingcart(browserInstance)
    shop_obj.click_checkout()
    pop_up.return_policy_popup()
    pop_up.pop_up_text()
    time.sleep(2)

def test_delivery_payment_information(browserInstance,home_fixture):
    pop_up=Orderpage(browserInstance)
    home_fixture.cart_link()
    shop_obj=Shoppingcart(browserInstance)
    shop_obj.click_checkout()
    assert pop_up.edit_shipping() ==" Delivery Information"
    assert pop_up.edit_payment() ==" Payment Information"
    assert pop_up.edit_cart()== " Shopping Cart"
    time.sleep(2)

def test_order_confirmation(browserInstance,home_fixture):
    pop_up=Orderpage(browserInstance)
    home_fixture.checkout_click()
    assert 'Processed' in pop_up.click_confirm_order()
    time.sleep(3)

    assert "Contact" in pop_up.order_id()

def test_order_history(browserInstance,home_fixture):
    pop_up=Orderpage(browserInstance)
    orderobj=Orderhistory(page=browserInstance)
    home_fixture.profile_tab_links()
    target_page=orderobj.validate_excel_data()
    assert  "Order" in target_page

def test_excel(browserInstance,home_fixture):
    orderobj=Orderhistory(page=browserInstance)
    home_fixture.profile_tab_links()
    orderobj.excel_products_quantity_view()

# @pytest.mark.regression
def test_export_order_excel(browserInstance,home_fixture):
    orderobj=Orderhistory(page=browserInstance)
    home_fixture.profile_tab_links()
    orderobj.export_total_excel()

# @pytest.mark.regression
def test_date_added_excel(browserInstance,home_fixture):
    orderobj=Orderhistory(page=browserInstance)
    home_fixture.profile_tab_links()
    orderobj.date_export_excel()

# @pytest.mark.regression
def test_status_info(browserInstance,home_fixture):
    orderobj=Orderhistory(page=browserInstance)
    home_fixture.profile_tab_links()
    orderobj.status_excel()

def test_click_back(browserInstance,home_fixture):
    pop_up=Orderpage(browserInstance)
    # Add items to cart before checkout
    home_fixture.cart_link()
    home_fixture.checkout_click()
    pop_up.click_back()

# # @pytest.mark.dependency(depends=['account_link'],scope='session')
# def test_logout_orderdetail(browserInstance,home_fixture):
#     test_account_link(browserInstance,home_fixture)
#     import_order=EnterOrder(browserInstance)
#     import_order.order_input()
#     time.sleep(3)

    




    








    

    
