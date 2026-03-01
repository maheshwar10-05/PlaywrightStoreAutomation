import pytest
# Note: time is no longer needed in async tests as Playwright handles waiting
from playwrightTestingPractice.pages.special_products import SpecialProducts


async def test_special_products(browserInstance, home_fixture):
    # Await the header link navigation
    await home_fixture.header_special_link()
    
    # Initialize the Page Object with the async browserInstance
    special_prod = SpecialProducts(browserInstance)
    
    # Await the method call
    await special_prod.products_special()


async def test_click_absolue_eye(browserInstance, home_fixture):
    await home_fixture.header_special_link()
    special_prod = SpecialProducts(browserInstance)
    
    # Await the method inside the assertion
    result = await special_prod.click_absolue_eye()
    assert "Absolue Eye" in result
    

async def test_click_ck_one_Summer(browserInstance, home_fixture):
    await home_fixture.header_special_link()
    special_prod = SpecialProducts(browserInstance)
    
    result = await special_prod.click_ck_one_summer()
    assert 'Summer' in result
    
@pytest.mark.asyncio
async def test_click_Replenishing_LipColour(browserInstance, home_fixture):
    await home_fixture.header_special_link()
    special_prod = SpecialProducts(browserInstance)
    
    result = await special_prod.click_replenishing_lipcolor()
    assert "Replenishing" in result
    
@pytest.mark.asyncio
async def test_click_creme_nuit(browserInstance, home_fixture):
    await home_fixture.header_special_link()
    special_prod = SpecialProducts(browserInstance)
    
    result = await special_prod.click_creme_nuit()
    # Note: Ensure "RAM" is actually expected in the product name 'Creme Precieuse Nuit'
    assert "Creme" in result