import time
import re
class Homepage:
    

    def __init__(self, page):
        self.page = page
        
    def homepage(self):
        headings = self.page.locator("span[class=maintext]")
        headings_list = []
        for i in range(headings.count()):
            head_names = headings.nth(i).text_content()
            headings_list.append(head_names)
        print(headings_list)
        return headings_list

    def product_from_heading_list_add_cart_home(self):
        products = self.page.locator("//div[@class='fixed']/a")
        add_cart_links = self.page.locator("//div[@class='col-md-3 col-sm-6 col-xs-12']")
        products_list = []
        items = self.homepage()

        for item in items:
            for i in range(products.count()):
                x = products.nth(i).text_content()
                products_list.append(x)
                if item == "Featured":
                    if x == 'Skinsheen Bronzer Stick':
                        add_cart_links.nth(i).get_by_title("Add to Cart").click()
                        element=self.page.locator("//div[@class='pricetag jumbotron added_to_cart']")
                        print(element.evaluate("el => getComputedStyle(el).getPropertyValue('background-color')"))
                        self.page.locator("//div[@class='quick_basket']").is_visible()
                        break
                elif item == "Latest Products":
                    if x == "Absolute Anti-Age Spot Replenishing Unifying TreatmentSPF 15":
                        add_cart_links.nth(i).get_by_title("Add to Cart").click()
                        element = self.page.locator("//div[@class='pricetag jumbotron added_to_cart']").first
                        print(element.evaluate("el => getComputedStyle(el).getPropertyValue('background-color')"))
                        self.page.locator("//div[@class='quick_basket']").first.is_visible()
                        break
                elif item == "Bestsellers":
                    if x == "New Ladies High Wedge Heel Toe Thong Diamante Flip Flop Sandals":
                        add_cart_links.nth(i).get_by_title("Add to Cart").click()
                        self.page.locator('a').filter(has_text="Home").first.click()
                        break

                elif item == "Specials":
                    if x == "Acqua Di Gio Pour Homme":
                        add_cart_links.nth(i).get_by_title("Add to Cart").click()
                        self.page.locator('a').filter(has_text="Home").first.click()
                        break
        cart_count=self.page.locator("//a[@class='dropdown-toggle']/span[@class='label label-orange font14']").text_content()
        print(products_list)
        return cart_count.strip()
    
    def hover_cart_items_home(self):
        self.page.locator("ul[class='nav topcart pull-left'] a[class='dropdown-toggle']").hover()
        self.page.locator('a.btn.btn-default').click()

    def shopping_cart_dipslay_from_home(self):
        cart_title=self.page.locator('span.maintext').text_content()
        print(cart_title)
        return cart_title
    
    def breadcomb_accessories_hover(self):
        accessories_dict={}
        list_access=[]
        accessories=self.page.locator("//ul[@class='nav-pills categorymenu']/li/a")
        for i in range(accessories.count()):
            accessories.nth(i).hover()
            a=accessories.nth(i).text_content()
            list_access.append(a.strip())
        accessories_dict["accessories"]=list_access
        return accessories_dict

    def sub_type_accessories(self):
        sub_accessories_home=self.page.locator("//ul[@id='main_menu']/li/a/span")
        sub_acc_list_home=[]
        sub_acc_dict_home={}
        sub_acc_dict={}
        accessories_dict=self.breadcomb_accessories_hover()
        print(accessories_dict)
        values1=list(accessories_dict.values())[0]
        print(values1)
        for value in values1:
              if value=="Home":
                try:
                    for m in range(sub_accessories_home.count()):
                        y=sub_accessories_home.nth(m).text_content()    
                        sub_acc_list_home.append(y)
                    sub_acc_dict_home["Home"]=sub_acc_list_home
                    print(sub_acc_dict_home)
                except:
                    print("Not valid")    
        new_list=[v for v in values1 if v !="Home" ]
        print(new_list)
        for index in range(2,len(values1)+1):
                sub_acc_list=[]   
                app=self.page.locator(f"//li[{index}]//div[1]//ul[1]//li/a")  
                for k in range(app.count()):
                            x=app.nth(k).text_content()
                            sub_acc_list.append(x.strip())
                sub_acc_dict[new_list[index-2]]=sub_acc_list               
        print(sub_acc_dict)
        return sub_acc_dict
    def click_any_sub_accessories(self):
    
        sub_acc_dict=self.sub_type_accessories()
        print(sub_acc_dict["Men"])
        list_acc=['Home', 'Apparel & accessories', 'Makeup', 'Skincare', 'Fragrance', 'Men', 'Hair Care', 'Books']
        for i in list_acc:
         if i=="Men":
          self.page.locator("//ul[@class='nav-pills categorymenu']/li/a").filter(has_text=i).hover()
          for j in sub_acc_dict["Men"]:
           if j=="Fragrance Sets":
            self.page.locator("//li[6]//div[1]//ul[1]//li/a").filter(has_text=j).click()
        sub_access_title=self.page.locator('span.maintext').text_content()
        time.sleep(3)
        return sub_access_title
        

    def currency_values(self):
        currency_list_actual=[]
        currency_elements=self.page.locator("//ul[@class='dropdown-menu currency']/li/a")
        for i in range(currency_elements.count()):
            x=currency_elements.nth(i).text_content()
            currency_list_actual.append(x)
        currency_list_actual_clean=[item.strip().replace("$","").strip() for item in currency_list_actual]
        self.page.locator("li.dropdown.hover").first.hover()
        currency_elements.filter(has_text="€ Euro").click()
        text=self.page.locator("//a[@class='dropdown-toggle']/span[1]").first.text_content()

        print(currency_list_actual_clean, text,"satisfied")
        return currency_list_actual_clean,text
    
    def search_keywords(self):
        self.page.get_by_placeholder("Search Keywords").click()
        keywords=self.page.locator("//li[@class='search-category']/a")
        list_keyword=[]
        for i in range(keywords.count()):
            x=keywords.nth(i).text_content()
            list_keyword.append(x)
        print(list_keyword)
        keywords.filter(has_text="Makeup").click()
        active_selected=self.page.locator("//li/a[@id='category_selected']").text_content()
        
        print(active_selected)
        screenshot_path=f"playwrightTesting/output/screenshots/test_search_keyword.png"
        self.page.screenshot(path=screenshot_path,full_page=True)
        return active_selected
    def search_page(self):
        self.page.get_by_title("Go").click()
        title=self.page.locator(".maintext").text_content()
        screenshot_path=f"playwrightTesting/output/screenshots/test_search_page.png"
        self.page.screenshot(path=screenshot_path,full_page=True)
        return title
    def new_tab_Abante_cart(self):
        with self.page.expect_popup() as page_info:
            self.page.get_by_title("Ideal OpenSource E-commerce Solution").click()
            abante_page=page_info.value
            new_page_title=abante_page.title()
            abante_page.screenshot(path="playwrightTesting/output/screenshots/test_abante_page.png",full_page=True)

            print(new_page_title)
            return new_page_title
        
    def abante_contribute(self):
        with self.page.expect_popup() as page_info:
            self.page.locator("//div[@class='b_block flt_right payment']/a").click()
            abante_contribute_page=page_info.value
            abante_contribute_page.screenshot(path="playwrightTesting/output/screenshots/test_contribute_page.png",full_page=True)
            heading=abante_contribute_page.locator(".h4.heading-title").text_content()
            return heading,abante_contribute_page
    def help_with_review(self):
        heading,abante_cont_page=self.abante_contribute()
        with abante_cont_page.expect_popup() as second_page_info:
            abante_cont_page.locator("//div/strong[2]/a").first.click()
            
            review_page=second_page_info.value
            heading2=review_page.locator("h2").first.text_content()
            review_page.screenshot(path="playwrightTesting/output/screenshots/test_review_page.png",full_page=True)
            print(heading2)
            return heading2
        
    def footer_page_content(self):
        footer_dict={}
        # footer_text=self.page.locator("//div[@id='block_frame_html_block_1775']/h2").text_content()
        footer_para=self.page.locator("div[id=block_frame_html_block_1775] p").text_content()
        contact_list=[]
        # footer_dict[footer_text]=footer_para.strip()
        # print(footer_dict)
        footer_contactus=self.page.locator("//div[@class='block_frame block_frame_html_block']/ul/li")
        footer_elements=self.page.locator("//div[@class='block_frame block_frame_html_block']/h2")
        names_testmonials=self.page.locator("//span[@class='pull-left orange']")
        feedback_content=self.page.locator("//ul[@class='slides']/li")
        testmonials={}
        feedback_content_list=[]
        testmonials_list=[]
        
        for i in range(footer_elements.count()):
            x=footer_elements.nth(i).text_content()
            footer_dict[x.strip()]=""
        for key,value in footer_dict.items():
            if key=="About Us":
                footer_dict[key]=footer_para.strip()
            elif key=="Contact Us":
                for i in range(footer_contactus.count()):
                    contact=footer_contactus.nth(i).text_content()
                    contact_list.append(contact.strip())
                footer_dict[key]=contact_list
            elif key=="Testimonials":
                
                for i in range(names_testmonials.count()):
                    y=names_testmonials.nth(i).text_content()
                    testmonials_list.append(y.strip())


                for j in range(feedback_content.count()):
                        x=feedback_content.nth(j).text_content()
                        feedback_content_list.append(x.strip())
                for p,q in zip(testmonials_list,feedback_content_list):
                    if p in q:
                        new_1=q.replace(p,"")
                    testmonials[p]=new_1.strip()
                footer_dict[key]=testmonials
                
    
                    
        print(footer_dict)
    def brand_scrolling_list(self):
        brand_list=[]
        brand_elements=self.page.locator("//ul[@id='brandcarousal']/li/div/a")
        for i in range(brand_elements.count()):
            brand_elements.nth(i).click()
            name_brand=self.page.locator(".maintext").text_content()
            brand_list.append(name_brand.strip())
            self.page.go_back()
        print(brand_list)
        return brand_list
    def products_each_brand(self):
        each_brand_product_dict={}
        brand_elements=self.page.locator("//ul[@id='brandcarousal']/li/div/a")
        

        for i in range(brand_elements.count()):
            product_names=[]
            brand_elements.nth(i).click()
            name_brand=self.page.locator(".maintext").text_content()
            product_brands=self.page.locator("//div[@class='col-md-3 col-sm-6 col-xs-12']/div[1]/div/a")
            for j in range(product_brands.count()):
                y=product_brands.nth(j).text_content()
                product_names.append(y.strip())
            self.page.go_back()
            each_brand_product_dict[name_brand.strip()]=product_names
                
        print(each_brand_product_dict)

    def cart_link(self):
        self.page.get_by_role("link",name="CART").first.click()
            

    def social_media_links(self):
        icon_list=[]
        icons=self.page.locator("div.social_icons").locator("a")
        for i in range(icons.count()):
            if i<3:

                current_icon=icons.nth(i)
                icon_text=current_icon.text_content()
                icon_list.append(icon_text)
                if icon_text in ['Facebook', 'Twitter']:
                    with self.page.expect_popup() as newpage:
                        current_icon.click()
                        media_page=newpage.value
                    print(media_page.title())
                        
                elif icon_text == 'Linkedin':
                    current_icon.click()
                    print(self.page.locator("span.sr-only").first.text_content())
                    self.page.go_back()
                    

    def checkout_click(self):
        try:
            # Wait for the main menu to be visible
            self.page.wait_for_selector("ul#main_menu_top", state="visible", timeout=10000)
            
            # Get all links in main menu and debug
            header_links = self.page.locator("ul#main_menu_top > li > a")
            count = header_links.count()
            print(f"\nTotal header links found: {count}")
            
            # Print all available links with their positions
            for i in range(count):
                link_text = header_links.nth(i).text_content().strip()
                href = header_links.nth(i).get_attribute("href")
                print(f"Link {i}: Text='{link_text}', Href='{href}'")
            
            # Find checkout by iterating and matching exact text
            checkout_index = -1
            for i in range(count):
                text = header_links.nth(i).text_content().strip()
                if text == "Checkout":
                    checkout_index = i
                    break
            
            if checkout_index >= 0:
                print(f"\nCheckout found at index {checkout_index}, clicking...")
                checkout_link = header_links.nth(checkout_index)
                checkout_link.wait_for(state="visible", timeout=10000)
                
                # Get the href to verify it's the right link
                href = checkout_link.get_attribute("href")
                print(f"Clicking checkout link with href: {href}")
                
                # Use JavaScript click to ensure it's clicked
                checkout_link.evaluate("el => el.click()")
                
                # Wait for page to load
                try:
                    self.page.wait_for_url("**/checkout/**", timeout=10000)
                    current_url = self.page.url
                    print(f"Successfully navigated to: {current_url}")
                except:
                    current_url = self.page.url
                    print(f"Navigation may have been redirected. Current URL: {current_url}")
                    
            else:
                raise Exception(f"Checkout link not found. Available links: {count}")
                
        except Exception as e:
            print(f"Error in checkout_click: {str(e)}")
            raise
            
            
            # self.page.go_back()

    def header_special_link(self):
        self.page.locator("//ul[@id='main_menu_top']/li/a").filter(has_text="Specials").click()
        header=self.page.locator(".maintext").text_content().strip()
        print(header)
        return header
    
    def header_account_link(self):
        self.page.locator("//ul[@id='main_menu_top']/li[@data-id='menu_account']").hover()
        time.sleep(1)
        self.page.locator("//li[@data-id='menu_account']/ul/li/a[@class='sub menu_logout']").first.click()
        self.page.locator("//ul[@id='main_menu_top']/li[@data-id='menu_account']").hover()
        self.page.locator("//li[@data-id='menu_account']/ul/li/a[@class='sub menu_order']").first.click()
        time.sleep(3)



          
            
                
        
        

    
    def women_foot_wear_error(self):
        self.page.get_by_role("link", name="New Ladies High Wedge Heel Toe Thong Diamante Flip Flop Sandals").click()
        time.sleep(3)
        self.page.get_by_role("link", name="Add to Cart").click()
        error_message=self.page.locator("div.alert.alert-error.alert-danger").text_content().strip()
        print(error_message)
        
        return error_message
    def fill_all_fields_footwear(self):
        elements=self.page.locator("//div[@class='col-md-6 text-center']//li/a")

        for i in range(elements.count()):
            elements.nth(i).click()
            time.sleep(2)

        self.page.get_by_role("radio", name="3 UK").click()
        self.page.locator("#option345").select_option("red")
        self.page.get_by_role("link", name="Add to wish list").click()
        self.page.get_by_role("link", name="Reviews (0)").click()
        self.page.locator("#rating4:visible").click()
        self.page.locator("#name").fill("Reviewer")
        self.page.locator("#text").fill("Good")
        time.sleep(10)
        self.page.get_by_role("button", name="Submit").click()

    def profile_tab_links(self):
        self.page.get_by_role("link", name="Welcome back tester123").hover()
        tab_links=self.page.locator("//ul[@class='sub_menu dropdown-menu']/li/a")
        tab_links.filter(has_text="Order History").click()
        
        time.sleep(3)

    

        

    

            





    

            
            
            
                






            




        

            
        
        

            

    



                   


            

                
     
        
        
 
        
        

          
                





        
        
        



        
        




