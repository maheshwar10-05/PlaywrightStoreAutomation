
from playwrightTestingPractice.pages.subaccessory_product_page import Subaccessory
from playwrightTestingPractice.pages.specific_product_page import Specificproduct


def test_various_sub_products(browserInstance,common_steps):
    homepage_categories,count1=common_steps
    headings_list=homepage_categories.homepage()
    sub_page=Subaccessory(browserInstance)
    homepage_categories.click_any_sub_accessories()
    sub_page.view_product()

def test_sub_product_page(browserInstance,common_steps,login_fixture):
    homepage_categories,count1=login_fixture
    headings_list=homepage_categories.homepage()
    sub_page=Subaccessory(browserInstance)
    sub_prod_page=Specificproduct(browserInstance)
    
    homepage_categories.click_any_sub_accessories()
    sub_page.view_product()
    sub_prod_page.product_specific()






