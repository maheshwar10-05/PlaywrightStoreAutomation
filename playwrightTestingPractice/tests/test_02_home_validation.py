from playwrightTestingPractice.testdata.testdata_file import categories_list,currency_list
from playwrightTestingPractice.pages.homepage import Homepage
import pytest

# Every test must be 'async def'
async def test_home_validation(browserInstance, home_fixture):
    # Await every POM method call
    headings_list = await home_fixture.homepage()
    cart_home_count = await home_fixture.product_from_heading_list_add_cart_home()
    
    assert headings_list == categories_list
    
    await home_fixture.hover_cart_items_home()
    # If the method returns a value used in an assertion, await it first
    display_text = await home_fixture.shopping_cart_dipslay_from_home()
    assert "Shopping" in display_text

async def test_home_breadcomb_accessories(browserInstance, home_fixture):
    await home_fixture.sub_type_accessories()

async def test_sub_accessories_click(browserInstance, home_fixture):
    result = await home_fixture.click_any_sub_accessories()
    assert "Fragrance" in result

async def test_currency(browserInstance, home_fixture):
    actual_list, text = await home_fixture.currency_values()
    for expected in currency_list:
        assert any(expected in actual for actual in actual_list)

    for currency_text in currency_list:
        if currency_text == text:
            print("satisfied")
            assert True

async def test_search_keywords(browserInstance, home_fixture):
    selected_keyword = await home_fixture.search_keywords()
    assert "Makeup" == selected_keyword
    title_page = await home_fixture.search_page()
    assert "Search" in title_page

async def test_abante_page(browserInstance, home_fixture):
    title = await home_fixture.new_tab_Abante_cart()
    assert title == "AbanteCart - Free Open Source Ecommerce Solution"

async def test_contribute_abante(browserInstance, home_fixture):
    heading, link = await home_fixture.abante_contribute()
    assert "AbanteCart Community and Contribution" in heading

async def test_abante_review(browserInstance, home_fixture):
    review_text = await home_fixture.help_with_review()
    assert "Write Review for AbanteCart" in review_text

async def test_footer_content(browserInstance, home_fixture):
    await home_fixture.footer_page_content()

async def test_brand_click(browserInstance, home_fixture):
    await home_fixture.brand_scrolling_list()

async def test_product_each_brand(browserInstance, home_fixture):
    await home_fixture.products_each_brand()

async def test_icon_click(browserInstance, home_fixture):
    await home_fixture.social_media_links()

async def test_women_footwear(browserInstance, home_fixture):
    error_msg = await home_fixture.women_foot_wear_error()
    assert "Please select all required options" in error_msg
    await home_fixture.fill_all_fields_footwear()

async def test_order_history(browserInstance, home_fixture):
    await home_fixture.profile_tab_links()

async def test_special_link(browserInstance, home_fixture):
    special_text = await home_fixture.header_special_link()
    assert "Special" in special_text
# @pytest.mark.dependency(name='account_link',scope='session')
# def test_account_link(browserInstance,home_fixture):
#     home_fixture
#     home_fixture.header_account_link()


    









    




