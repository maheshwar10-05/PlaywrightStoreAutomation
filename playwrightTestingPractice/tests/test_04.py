
from playwrightTestingPractice.pages.subaccessory_product_page import Subaccessory
from playwrightTestingPractice.pages.specific_product_page import Specificproduct


def test_various_sub_products(browserInstance,home_fixture):
    headings_list=home_fixture.homepage()
    sub_page=Subaccessory(browserInstance)
    home_fixture.click_any_sub_accessories()
    sub_page.view_product()

def test_sub_product_page(browserInstance,home_fixture):

    headings_list=home_fixture.homepage()
    sub_page=Subaccessory(browserInstance)
    sub_prod_page=Specificproduct(browserInstance)
    
    home_fixture.click_any_sub_accessories()
    sub_page.view_product()
    sub_prod_page.product_specific()






