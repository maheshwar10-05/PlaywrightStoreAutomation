import time,pytest
from playwrightTestingPractice.utils.utility import user_credentials,user_login

from playwrightTestingPractice.pages.homepage import Homepage
from playwrightTestingPractice.pages.checkout_information_order_confirmation_page import Orderpage
from playwrightTestingPractice.pages.shoppingcart import Shoppingcart
from playwrightTestingPractice.pages.orderhistory import Orderhistory
from playwrightTestingPractice.pages.logout_orderdetails_entry import EnterOrder
from playwrightTestingPractice.pages.special_products import SpecialProducts
from playwrightTestingPractice.pages.replinishing import Replinishing

@pytest.fixture
async def replinishing_lip(browserInstance, home_fixture):
    """
    This fixture replaces the imported test. 
    It handles the navigation to the specific product page.
    """
    await home_fixture.header_special_link()
    special_prod = SpecialProducts(browserInstance)
    await special_prod.click_replenishing_lipcolor()
    return Replinishing(browserInstance)

async def test_input_quantity_special(replinishing_lip):
    # 'absolue_eye_page' is already navigated and initialized by the fixture
    total_price, single_price, updated_quantity = await replinishing_lip.input_quantity_special_replinishing()
    
    # Mathematical assertion
    assert total_price == single_price * int(updated_quantity)


async def test_click_add_cart_absolue_eye(replinishing_lip):
    result = await replinishing_lip.click_add_cart_replinishing()
    assert "Shopping" in result


async def test_model_number_replinishing(replinishing_lip):
    # Since this is an extraction, we just await it
    await replinishing_lip.extract_model_number_replinishing()


async def test_click_lancome_brand(replinishing_lip):
    result = await replinishing_lip.click_lancome_brand()
    assert "Lan" in result
    