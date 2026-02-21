from playwrightTestingPractice.testdata.testdata_file import categories_list,currency_list
from playwrightTestingPractice.pages.homepage import Homepage
import pytest

def test_home_validation(browserInstance,home_fixture):
    headings_list=home_fixture.homepage()
    cart_home_count=home_fixture.product_from_heading_list_add_cart_home()
    assert headings_list==categories_list
    # assert int(count1)+2 == int(cart_home_count)
    home_fixture.hover_cart_items_home()
    assert "Shopping" in home_fixture.shopping_cart_dipslay_from_home()

def test_home_breadcomb_accessories(browserInstance,home_fixture):
    home_fixture.sub_type_accessories()

def test_sub_accessories_click(browserInstance,home_fixture):
    assert "Fragrance" in home_fixture.click_any_sub_accessories()

def test_currency(browserInstance,home_fixture):
    actual_list,text= home_fixture.currency_values()
    for expected in currency_list:
        assert any(expected in actual for actual in actual_list)

    for currency_text in currency_list:
        if currency_text == text:
            print("satisfied")
            assert True

    
def test_search_keywords(browserInstance,home_fixture):
    selected_keyword=home_fixture.search_keywords()
    assert "Makeup"==selected_keyword
    title_page=home_fixture.search_page()
    assert "Search" in title_page

def test_abante_page(browserInstance,home_fixture):
    assert home_fixture.new_tab_Abante_cart()=="AbanteCart - Free Open Source Ecommerce Solution"

def test_contribute_abante(browserInstance,home_fixture):
    heading,link=home_fixture.abante_contribute()
    assert "AbanteCart Community and Contribution" in heading

def test_abante_review(browserInstance,home_fixture):
    assert "Write Review for AbanteCart" in home_fixture.help_with_review()

def test_footer_content(browserInstance,home_fixture):
    home_fixture.footer_page_content()
def test_brand_click(browserInstance,home_fixture):
    home_fixture.brand_scrolling_list()
def test_product_each_brand(browserInstance,home_fixture):
    home_fixture.products_each_brand()
def test_icon_click(browserInstance,home_fixture):
    home_fixture.social_media_links()

def test_women_footwear(browserInstance,home_fixture):
    assert "Please select all required options" in home_fixture.women_foot_wear_error()
    home_fixture.fill_all_fields_footwear()

def test_order_history(browserInstance,home_fixture):
    home_fixture.profile_tab_links()

def test_special_link(browserInstance,home_fixture):
    assert "Special" in home_fixture.header_special_link()

# @pytest.mark.dependency(name='account_link',scope='session')
# def test_account_link(browserInstance,home_fixture):
#     home_fixture
#     home_fixture.header_account_link()


    









    




