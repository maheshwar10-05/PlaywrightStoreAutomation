import asyncio
import re
from playwright.async_api import Page

class Homepage:
    def __init__(self, page: Page):
        self.page = page
        
        # --- LOCATORS ---
        self.main_headings = self.page.locator("span[class=maintext]")
        self.product_links = self.page.locator("//div[@class='fixed']/a")
        self.add_cart_containers = self.page.locator("//div[@class='col-md-3 col-sm-6 col-xs-12']")
        self.cart_total_label = self.page.locator("//a[@class='dropdown-toggle']/span[@class='label label-orange font14']")
        self.top_cart_toggle = self.page.locator("ul[class='nav topcart pull-left'] a[class='dropdown-toggle']")
        self.cart_checkout_btn = self.page.locator('a.btn.btn-default')
        self.category_pills = self.page.locator("//ul[@class='nav-pills categorymenu']/li/a")
        self.main_menu_spans = self.page.locator("//ul[@id='main_menu']/li/a/span")
        self.currency_dropdown = self.page.locator("//ul[@class='dropdown-menu currency']/li/a")
        self.currency_toggle = self.page.locator("li.dropdown.hover").first
        self.search_input = self.page.get_by_placeholder("Search Keywords")
        self.search_categories = self.page.locator("//li[@class='search-category']/a")
        self.search_go_btn = self.page.get_by_title("Go")
        self.abante_logo_link = self.page.get_by_title("Ideal OpenSource E-commerce Solution")
        self.footer_about_para = self.page.locator("div[id=block_frame_html_block_1775] p")
        self.footer_contact_items = self.page.locator("//div[@class='block_frame block_frame_html_block']/ul/li")
        self.footer_headers = self.page.locator("//div[@class='block_frame block_frame_html_block']/h2")
        self.brand_links = self.page.locator("//ul[@id='brandcarousal']/li/div/a")
        self.social_icons = self.page.locator("div.social_icons").locator("a")
        self.main_menu_top = self.page.locator("ul#main_menu_top")
        self.main_menu_top_links = self.page.locator("ul#main_menu_top > li > a")
        self.welcome_menu = self.page.get_by_role("link", name=re.compile(r"Welcome back", re.IGNORECASE))
        self.testimonial_names = self.page.locator("//span[@class='pull-left orange']")
        self.feedback_slides = self.page.locator("//ul[@class='slides']/li")
        self.footwear_product_link = self.page.get_by_role("link", name="New Ladies High Wedge Heel Toe Thong Diamante Flip Flop Sandals")
        self.footwear_options = self.page.locator("//div[@class='col-md-6 text-center']//li/a")
        self.error_alert = self.page.locator("div.alert.alert-error.alert-danger")
        self.profile_sublinks = self.page.locator("//ul[@class='sub_menu dropdown-menu']/li/a")
        self.timeout=page.wait_for_timeout(5000)
    # --- METHODS ---

    async def homepage(self):
        count = await self.main_headings.count()
        headings_list = []
        for i in range(count):
            head_names = await self.main_headings.nth(i).text_content()
            headings_list.append(head_names)
        print(headings_list)
        return headings_list

    async def product_from_heading_list_add_cart_home(self):
        products_list = [text.strip() for text in await self.product_links.all_text_contents()]
        items = await self.homepage()
        for item in items:
            for i,product_text in enumerate(products_list):

                
                if item == "Featured" and product_text == 'Skinsheen Bronzer Stick':
                    await self.add_cart_containers.nth(i).get_by_title("Add to Cart").click()
                    element = self.page.locator("//div[@class='pricetag jumbotron added_to_cart']")
                    print(await element.evaluate("el => getComputedStyle(el).getPropertyValue('background-color')"))
                    await self.page.locator("//div[@class='quick_basket']").is_visible()
                    break
                elif item == "Latest Products" and product_text == "Absolute Anti-Age Spot Replenishing Unifying TreatmentSPF 15":
                    await self.add_cart_containers.nth(i).get_by_title("Add to Cart").click()
                    element = self.page.locator("//div[@class='pricetag jumbotron added_to_cart']").first
                    print(await element.evaluate("el => getComputedStyle(el).getPropertyValue('background-color')"))
                    await self.page.locator("//div[@class='quick_basket']").first.is_visible()
                    break
                elif item == "Bestsellers" and product_text == "New Ladies High Wedge Heel Toe Thong Diamante Flip Flop Sandals":
                    await self.add_cart_containers.nth(i).get_by_title("Add to Cart").click()
                    await self.page.locator('a').filter(has_text="Home").first.click()
                    break
                elif item == "Specials" and product_text == "Acqua Di Gio Pour Homme":
                    await self.add_cart_containers.nth(i).get_by_title("Add to Cart").click()
                    await self.page.locator('a').filter(has_text="Home").first.click()
                    break
        
        cart_count = await self.cart_total_label.text_content()
        print(products_list)
        return cart_count.strip() if cart_count else "0"
    
    async def hover_cart_items_home(self):
        await self.top_cart_toggle.hover()
        await self.cart_checkout_btn.click()

    async def shopping_cart_dipslay_from_home(self):
        cart_title = await self.page.locator('span.maintext').text_content()
        print(cart_title)
        return cart_title
    
    async def breadcomb_accessories_hover(self):
        accessories_dict = {}
        list_access = []
        count = await self.category_pills.count()
        for i in range(count):
            await self.category_pills.nth(i).hover()
            a = await self.category_pills.nth(i).text_content()
            list_access.append(a.strip())
        accessories_dict["accessories"] = list_access
        return accessories_dict

    async def sub_type_accessories(self):
        sub_acc_list_home = []
        sub_acc_dict_home = {}
        sub_acc_dict = {}
        accessories_dict = await self.breadcomb_accessories_hover()
        values1 = list(accessories_dict.values())[0]
        
        for value in values1:
            if value == "Home":
                try:
                    count = await self.main_menu_spans.count()
                    for m in range(count):
                        y = await self.main_menu_spans.nth(m).text_content()    
                        sub_acc_list_home.append(y)
                    sub_acc_dict_home["Home"] = sub_acc_list_home
                except:
                    print("Not valid")    
        
        new_list = [v for v in values1 if v != "Home"]
        for index in range(2, len(values1) + 1):
            sub_acc_list = []   
            app = self.page.locator(f"//li[{index}]//div[1]//ul[1]//li/a")
            app_count = await app.count()
            for k in range(app_count):
                x = await app.nth(k).text_content()
                sub_acc_list.append(x.strip())
            sub_acc_dict[new_list[index-2]] = sub_acc_list               
        return sub_acc_dict

    async def click_any_sub_accessories(self):
        sub_acc_dict = await self.sub_type_accessories()
        list_acc = ['Home', 'Apparel & accessories', 'Makeup', 'Skincare', 'Fragrance', 'Men', 'Hair Care', 'Books']
        for i in list_acc:
            if i == "Men":
                await self.category_pills.filter(has_text=i).hover()
                for j in sub_acc_dict["Men"]:
                    if j == "Fragrance Sets":
                        await self.page.locator("//li[6]//div[1]//ul[1]//li/a").filter(has_text=j).click()
        sub_access_title = await self.page.locator('span.maintext').text_content()
        return sub_access_title
        
    async def currency_values(self):
        currency_list_actual = []
        count = await self.currency_dropdown.count()
        for i in range(count):
            x = await self.currency_dropdown.nth(i).text_content()
            currency_list_actual.append(x)
        currency_list_actual_clean = [item.strip().replace("$","").strip() for item in currency_list_actual]
        await self.currency_toggle.hover()
        await self.currency_dropdown.filter(has_text="€ Euro").click()
        text = await self.page.locator("//a[@class='dropdown-toggle']/span[1]").first.text_content()
        return currency_list_actual_clean, text
    
    async def search_keywords(self):
        await self.search_input.click()
        count = await self.search_categories.count()
        list_keyword = []
        for i in range(count):
            x = await self.search_categories.nth(i).text_content()
            list_keyword.append(x)
        await self.search_categories.filter(has_text="Makeup").click()
        active_selected = await self.page.locator("//li/a[@id='category_selected']").text_content()
        await self.page.screenshot(path="reports/screenshots/test_search_keyword.png", full_page=True)
        return active_selected

    async def search_page(self):
        await self.search_go_btn.click()
        title = await self.page.locator(".maintext").text_content()
        await self.page.screenshot(path="reports/screenshots/test_search_page.png", full_page=True)
        return title

    async def new_tab_Abante_cart(self):
        async with self.page.expect_popup() as page_info:
            await self.abante_logo_link.click()
        abante_page = await page_info.value
        new_page_title = await abante_page.title()
        await abante_page.screenshot(path="reports/screenshots/test_abante_page.png", full_page=True)
        return new_page_title
        
    async def abante_contribute(self):
        async with self.page.expect_popup() as page_info:
            await self.page.locator("//div[@class='b_block flt_right payment']/a").click()
        abante_contribute_page = await page_info.value
        await abante_contribute_page.screenshot(path="reports/screenshots/test_contribute_page.png", full_page=True)
        heading = await abante_contribute_page.locator(".h4.heading-title").text_content()
        return heading, abante_contribute_page

    async def help_with_review(self):
        heading, abante_cont_page = await self.abante_contribute()
        async with abante_cont_page.expect_popup() as second_page_info:
            await abante_cont_page.locator("//div/strong[2]/a").first.click()
        review_page = await second_page_info.value
        heading2 = await review_page.locator("h2").first.text_content()
        await review_page.screenshot(path="reports/screenshots/test_review_page.png", full_page=True)
        return heading2
        
    async def footer_page_content(self):
        footer_dict = {}
        footer_para = await self.footer_about_para.text_content()
        contact_list = []
        count = await self.footer_headers.count()
        for i in range(count):
            x = await self.footer_headers.nth(i).text_content()
            footer_dict[x.strip()] = ""
        for key, value in footer_dict.items():
            if key == "About Us":
                footer_dict[key] = footer_para.strip()
            elif key == "Contact Us":
                c_count = await self.footer_contact_items.count()
                for i in range(c_count):
                    contact = await self.footer_contact_items.nth(i).text_content()
                    contact_list.append(contact.strip())
                footer_dict[key] = contact_list
            elif key == "Testimonials":
                testmonials_list = []
                feedback_content_list = []
                t_count = await self.testimonial_names.count()
                for i in range(t_count):
                    y = await self.testimonial_names.nth(i).text_content()
                    testmonials_list.append(y.strip())
                f_count = await self.feedback_slides.count()
                for j in range(f_count):
                    x = await self.feedback_slides.nth(j).text_content()
                    feedback_content_list.append(x.strip())
                testmonials = {}
                for p, q in zip(testmonials_list, feedback_content_list):
                    new_1 = q.replace(p, "") if p in q else q
                    testmonials[p] = new_1.strip()
                footer_dict[key] = testmonials
        print(footer_dict)

    async def brand_scrolling_list(self):
        brand_list = []
        count = await self.brand_links.count()
        for i in range(count):
            await self.brand_links.nth(i).click()
            await self.timeout
            name_brand = self.page.locator(".maintext")
            brand_list.append((await name_brand.text_content()).strip())
            await self.page.go_back()
        return brand_list

    async def products_each_brand(self):
        each_brand_product_dict = {}
        count = await self.brand_links.count()
        for i in range(count):
            product_names = []
            await self.brand_links.nth(i).click()
            name_brand = await self.page.locator(".maintext").text_content()
            product_brands = self.page.locator("//div[@class='col-md-3 col-sm-6 col-xs-12']/div[1]/div/a")
            p_count = await product_brands.count()
            for j in range(p_count):
                y = await product_brands.nth(j).text_content()
                product_names.append(y.strip())
            await self.page.go_back()
            each_brand_product_dict[name_brand.strip()] = product_names
        print(each_brand_product_dict)

    async def cart_link(self):
        await self.page.get_by_role("link", name="CART").first.click()

    async def social_media_links(self):
        count = await self.social_icons.count()
        for i in range(count):
            if i < 3:
                current_icon = self.social_icons.nth(i)
                icon_text = await current_icon.text_content()
                if icon_text in ['Facebook', 'Twitter']:
                    async with self.page.expect_popup() as newpage:
                        await current_icon.click()
                    media_page = await newpage.value
                    print(await media_page.title())
                elif icon_text == 'Linkedin':
                    await current_icon.click()
                    linkedin_text = await self.page.locator("span.sr-only").first.text_content()
                    print(linkedin_text)
                    await self.page.go_back()

    async def checkout_click(self):
        await self.page.wait_for_selector("ul#main_menu_top", state="visible", timeout=10000)
        count = await self.main_menu_top_links.count()
        checkout_index = -1
        for i in range(count):
            text = await self.main_menu_top_links.nth(i).text_content()
            if text.strip() == "Checkout":
                checkout_index = i
                break
        if checkout_index >= 0:
            checkout_link = self.main_menu_top_links.nth(checkout_index)
            await checkout_link.evaluate("el => el.click()")
            await self.page.wait_for_url("**/checkout/**", timeout=10000)

    async def header_special_link(self):
        await self.main_menu_top_links.filter(has_text="Specials").click()
        header = await self.page.locator(".maintext").text_content()
        return header.strip()

    async def women_foot_wear_error(self):
        await self.footwear_product_link.click()
        await self.page.get_by_role("link", name="Add to Cart").click()
        error_message = await self.error_alert.text_content()
        return error_message.strip()

    async def fill_all_fields_footwear(self):
        count = await self.footwear_options.count()
        for i in range(count):
            await self.footwear_options.nth(i).click()
            await self.page.wait_for_timeout(1000) # Replaced time.sleep with async wait
        await self.page.get_by_role("radio", name="3 UK").click()
        await self.page.locator("#option345").select_option("red")
        await self.page.get_by_role("link", name="Add to wish list").click()
        await self.page.get_by_role("link", name="Reviews (0)").click()
        await self.page.locator("#rating4:visible").click()
        await self.page.locator("#name").fill("Reviewer")
        await self.page.locator("#text").fill("Good")
        await self.page.get_by_role("button", name="Submit").click()

    async def profile_tab_links(self):
        await self.welcome_menu.hover()
        await self.profile_sublinks.filter(has_text="Order History").click()