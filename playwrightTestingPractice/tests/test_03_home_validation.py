from playwrightTestingPractice.testdata.testdata_file import categories_list,currency_list
import pytest

def test_home_validation(common_steps,login_fixture,browserInstance):
    homepage_categories,count1=login_fixture
    headings_list=homepage_categories.homepage()
    cart_home_count=homepage_categories.product_from_heading_list_add_cart_home()
    assert headings_list==categories_list
    assert int(count1)+2 == int(cart_home_count)
    homepage_categories.hover_cart_items_home()
    assert "Shopping" in homepage_categories.shopping_cart_dipslay_from_home()

def test_home_breadcomb_accessories(common_steps):
    homepage_categories,count1=common_steps
    homepage_categories.sub_type_accessories()

def test_sub_accessories_click(common_steps,login_fixture):
    homepage_categories,count1=login_fixture
    
    assert "Fragrance" in homepage_categories.click_any_sub_accessories()

def test_currency(common_steps):
    homepage_categories,count1=common_steps
    actual_list,text= homepage_categories.currency_values()
    for expected in currency_list:
        assert any(expected in actual for actual in actual_list)

    for currency_text in currency_list:
        if currency_text == text:
            print("satisfied")
            assert True

    
def test_search_keywords(common_steps):
    homepage_categories,count1=common_steps
    selected_keyword=homepage_categories.search_keywords()
    assert "Makeup"==selected_keyword
    title_page=homepage_categories.search_page()
    assert "Search" in title_page

def test_abante_page(common_steps):
    homepage_categories,count1=common_steps
    assert homepage_categories.new_tab_Abante_cart()=="AbanteCart - Free Open Source Ecommerce Solution"

def test_contribute_abante(common_steps):
    homepage_categories,count1=common_steps
    heading,link=homepage_categories.abante_contribute()
    assert "AbanteCart Community and Contribution" in heading

def test_abante_review(common_steps):
    homepage_categories,count1=common_steps
    assert "Write Review for AbanteCart" in homepage_categories.help_with_review()

def test_footer_content(common_steps):
    homepage_categories,count1=common_steps
    homepage_categories.footer_page_content()
def test_brand_click(common_steps):
    homepage_categories,count1=common_steps
    homepage_categories.brand_scrolling_list()
def test_product_each_brand(common_steps):
    homepage_categories,count1=common_steps
    homepage_categories.products_each_brand()
def test_icon_click(browserInstance,common_steps):
    homepage_categories,count1=common_steps
    homepage_categories.social_media_links()

def test_women_footwear(browserInstance,common_steps,login_fixture):
    homepage_categories,count1=login_fixture
    
    assert "Please select all required options" in homepage_categories.women_foot_wear_error()
    homepage_categories.fill_all_fields_footwear()

def test_order_history(browserInstance,common_steps,login_fixture):
    homepage_categories,count1=login_fixture
    homepage_categories.profile_tab_links()

def test_special_link(browserInstance,common_steps,login_fixture):
    homepage_categories,count1=login_fixture
    assert "Special" in homepage_categories.header_special_link()

@pytest.mark.dependency(name='account_link',scope='session')
def test_account_link(browserInstance,common_steps,login_fixture):
    homepage_categories,count1=login_fixture
    homepage_categories.header_account_link()


    









    




