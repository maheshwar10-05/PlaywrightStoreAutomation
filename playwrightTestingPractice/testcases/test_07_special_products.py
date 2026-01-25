import time,pytest
from playwrightTestingPractice.Utilities.utility import user_credentials,user_login

from playwrightTestingPractice.pageobjects.homepage import Homepage
from playwrightTestingPractice.pageobjects.checkout_information_order_confirmation_page import Orderpage
from playwrightTestingPractice.pageobjects.shoppingcart import Shoppingcart
from playwrightTestingPractice.pageobjects.orderhistory import Orderhistory
from playwrightTestingPractice.pageobjects.logout_orderdetails_entry import EnterOrder
from playwrightTestingPractice.pageobjects.special_products import SpecialProducts

def test_special_products(browserInstance,common_steps,login_fixture):
    homepage_categories,count1=login_fixture
    homepage_categories.header_special_link()
    special_prod=SpecialProducts(browserInstance)
    special_prod.products_special()

def test_click_absolue_eye(browserInstance,common_steps,login_fixture):
    homepage_categories,count1=login_fixture

    homepage_categories.header_special_link()
    special_prod=SpecialProducts(browserInstance)
    assert "Absolue Eye" in special_prod.click_absolue_eye()
    
def test_input_quantity_special(browserInstance,common_steps,login_fixture):
    test_click_absolue_eye(browserInstance,common_steps,login_fixture)
    special_prod=SpecialProducts(browserInstance)
    
    total_price,single_price,updated_quantity=special_prod.input_quantity_special()
    assert total_price==single_price*int(updated_quantity)
    
    
    
