import pytest
from playwrightTestingPractice.pages.subaccessory_product_page import Subaccessory
from playwrightTestingPractice.pages.specific_product_page import Specificproduct


async def test_various_sub_products(browserInstance, home_fixture):
    # Rule 1: Always await methods that return data or perform actions
    headings_list = await home_fixture.homepage()
    
    # Initialize your other Page Objects
    sub_page = Subaccessory(browserInstance)
    
    # Rule 2: Methods that interact with the browser must be awaited
    await home_fixture.click_any_sub_accessories()
    await sub_page.view_product()


async def test_sub_product_page(browserInstance, home_fixture):
    # Rule 1: Await the data retrieval
    headings_list = await home_fixture.homepage()
    
    # Initialize Page Objects
    sub_page = Subaccessory(browserInstance)
    sub_prod_page = Specificproduct(browserInstance)
    
    # Rule 2: Await the sequence of actions
    await home_fixture.click_any_sub_accessories()
    await sub_page.view_product()
    await sub_prod_page.product_specific()
