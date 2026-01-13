import re,time
import pandas as pd
class Orderpage:
    def __init__(self,page) -> None:
        self.page=page    

    def order_confirmation_page(self):
        heading_oredr_confirmation=self.page.locator("span.maintext").text_content()
        return heading_oredr_confirmation
    
    def return_policy_popup(self):
        self.page.get_by_role("link", name="Return Policy").first.click()
    def pop_up_text(self):
        policy_dict={}
        web_ele=self.page.locator("//div[@class='middle']/p").first.text_content()
        web_ele2=self.page.locator("//div[@class='middle']/p").last.text_content()
        policy_dict[web_ele]=web_ele2
        print(policy_dict)
        self.page.get_by_text("Close").first.click()

    def edit_shipping(self):
        self.page.get_by_role("link", name="Edit Shipping").click()
        title_target_page=self.page.locator("//span[@class='maintext']").text_content()
        self.page.go_back()
    
        return title_target_page
    def edit_payment(self):
        self.page.get_by_role("link", name="Edit Payment").click()
        title_target_page=self.page.locator("span.maintext").text_content()
        self.page.go_back()
        return title_target_page
    def edit_cart(self):
        self.page.get_by_role("link", name="Edit Cart").click()
        page_title= self.page.locator("span.maintext").text_content()
        return page_title
    
    def click_confirm_order(self):

        self.page.get_by_text("Confirm Order", exact=True).click()
        order_success_page=self.page.locator("//span[@class='maintext']")
        order_success_page.wait_for(state="visible")
        success=order_success_page.text_content().strip()
        print(success)

        return success
    
    def order_id(self):
        order_list=[]
        symbols=['#']
        web_el=self.page.locator("//section[@class='mb40']/p")
        for i in range(web_el.count()):
            a=web_el.nth(i).text_content().strip()
            order_list.append(a)
        print(order_list)
        for i in order_list:
             x=re.search(r'\d{5}',i)
             if x:
                k=x.group()
                print(k)
             y=re.search(r'store owner',i)
             if y:
                 z=y.group()
                 print(z)
                 self.page.get_by_role("link", name="store owner").click()
        time.sleep(3)
        contact_page_text=self.page.locator(".maintext").text_content().strip()
        
        # Get the full raw text content
        raw_content = self.page.locator("//div[@class='col-md-6 pull-left']").text_content()

        # Split the text into lines, strip whitespace from each line, and filter out empty lines
        cleaned_lines = [line.strip() for line in raw_content.splitlines() if line.strip()]

        # Join them back with newlines or print individually
        address_title = "\n".join(cleaned_lines)

        print(address_title)

        return contact_page_text
    
                 
        # list1=[]
        # list1.append({'order_id':k})
        # df=pd.DataFrame(list1)
        # df.to_excel("test_results1.xlsx", index=False)

        print("Data exported successfully!")
        
    def func(self):

        assert False

        
    

                    



