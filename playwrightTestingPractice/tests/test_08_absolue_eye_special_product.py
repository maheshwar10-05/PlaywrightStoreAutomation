import time,pytest
from playwrightTestingPractice.utils.utility import user_credentials,user_login

from playwrightTestingPractice.pages.homepage import Homepage
from playwrightTestingPractice.pages.checkout_information_order_confirmation_page import Orderpage
from playwrightTestingPractice.pages.shoppingcart import Shoppingcart
from playwrightTestingPractice.pages.orderhistory import Orderhistory
from playwrightTestingPractice.pages.logout_orderdetails_entry import EnterOrder
from playwrightTestingPractice.pages.special_products import SpecialProducts
from playwrightTestingPractice.pages.absolue_eye_special import AbsolueEye
from playwrightTestingPractice.tests.test_07_special_products import test_click_absolue_eye 

def test_input_quantity_special(browserInstance,common_steps,login_fixture):
    test_click_absolue_eye(browserInstance,common_steps,login_fixture)
    absolue_prod_eye=AbsolueEye(browserInstance)
    
    total_price,single_price,updated_quantity=absolue_prod_eye.input_quantity_special_absolue_eye()
    assert total_price==single_price*int(updated_quantity)
    
def test_click_add_cart_absolue_eye(browserInstance,common_steps,login_fixture):
    test_click_absolue_eye(browserInstance,common_steps,login_fixture)
    absolue_prod_eye=AbsolueEye(browserInstance)
    assert "Shopping" in absolue_prod_eye.click_add_cart_absolue_eye()
    
def test_model_number_absolue_eye(browserInstance,common_steps,login_fixture):
    test_click_absolue_eye(browserInstance,common_steps,login_fixture)
    absolue_prod_eye=AbsolueEye(browserInstance)
    absolue_prod_eye.extract_model_number_absolue_eye()
    
def test_click_lancome_brand(browserInstance,common_steps,login_fixture):
    test_click_absolue_eye(browserInstance,common_steps,login_fixture)
    absolue_prod_eye=AbsolueEye(browserInstance)
    assert "Lan" in absolue_prod_eye.click_lancome_brand()