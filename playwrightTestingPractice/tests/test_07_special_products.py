import time,pytest
from playwrightTestingPractice.utils.utility import user_credentials,user_login

from playwrightTestingPractice.pages.homepage import Homepage
from playwrightTestingPractice.pages.checkout_information_order_confirmation_page import Orderpage
from playwrightTestingPractice.pages.shoppingcart import Shoppingcart
from playwrightTestingPractice.pages.orderhistory import Orderhistory
from playwrightTestingPractice.pages.logout_orderdetails_entry import EnterOrder
from playwrightTestingPractice.pages.special_products import SpecialProducts

def test_special_products(browserInstance,click_login_register_button,login_fixture):
    homepage_categories,count1=login_fixture
    homepage_categories.header_special_link()
    special_prod=SpecialProducts(browserInstance)
    special_prod.products_special()

def test_click_absolue_eye(browserInstance,common_steps,login_fixture):
    homepage_categories,count1=login_fixture

    homepage_categories.header_special_link()
    special_prod=SpecialProducts(browserInstance)
    assert "Absolue Eye" in special_prod.click_absolue_eye()
    
def test_click_ck_one_Summer(browserInstance,common_steps,login_fixture):
    homepage_categories,count1=login_fixture

    homepage_categories.header_special_link()
    special_prod=SpecialProducts(browserInstance)
    assert 'Summer' in special_prod.click_ck_one_summer()
    
    
def test_click_Replenishing_LipColour(browserInstance,common_steps,login_fixture):
    homepage_categories,count1=login_fixture

    homepage_categories.header_special_link()
    special_prod=SpecialProducts(browserInstance)
    assert "Replenishing" in special_prod.click_replenishing_lipcolor()
    
def test_click_creme_nuit(browserInstance,common_steps,login_fixture):
    homepage_categories,count1=login_fixture

    homepage_categories.header_special_link()
    special_prod=SpecialProducts(browserInstance)
    
    assert "Creme" in special_prod.click_creme_nuit()
    
    
    
    
    

    

    
