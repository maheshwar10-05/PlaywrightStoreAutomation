import pytest
from playwrightTestingPractice.pages.special_products import SpecialProducts
from playwrightTestingPractice.pages.absolue_eye_special import AbsolueEye

# -------------------------
# SHARED FIXTURE (The Best Practice way)
# -------------------------
@pytest.fixture
async def absolue_eye_page(browserInstance, home_fixture):
    """
    This fixture replaces the imported test. 
    It handles the navigation to the specific product page.
    """
    await home_fixture.header_special_link()
    special_prod = SpecialProducts(browserInstance)
    await special_prod.click_absolue_eye()
    return AbsolueEye(browserInstance)

# -------------------------
# ASYNC TESTS
# -------------------------


async def test_input_quantity_special(absolue_eye_page):
    # 'absolue_eye_page' is already navigated and initialized by the fixture
    total_price, single_price, updated_quantity = await absolue_eye_page.input_quantity_special_absolue_eye()
    
    # Mathematical assertion
    assert total_price == single_price * int(updated_quantity)


async def test_click_add_cart_absolue_eye(absolue_eye_page):
    result = await absolue_eye_page.click_add_cart_absolue_eye()
    assert "Shopping" in result


async def test_model_number_absolue_eye(absolue_eye_page):
    # Since this is an extraction, we just await it
    await absolue_eye_page.extract_model_number_absolue_eye()


async def test_click_lancome_brand(absolue_eye_page):
    result = await absolue_eye_page.click_lancome_brand()
    assert "Lan" in result