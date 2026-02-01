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
        time.sleep(5)
        order_success_page=self.page.locator(".maintext")
        order_success_page.wait_for(state="visible")
        success=order_success_page.text_content().strip()
        print(success)

        return success
    
    def order_id(self):
        # 1. Use a more robust locator for the success message container
        # This waits for the section to actually exist in the DOM
        container = self.page.locator("section.mb40")
        container.wait_for(state="visible")

        # 2. Extract all <p> tags inside that section
        # We use .all() to get a list of locator objects we can iterate over
        paragraphs = container.locator("p").all()
        
        # 3. Clean and append to a list
        order_list = [p.text_content().strip() for p in paragraphs]
        
        # Debug print to verify the list is no longer empty
        print(f"Extracted Lines: {order_list}")

        # 4. Logic to click 'store owner' if it exists in the list
        for line in order_list:
            if "#" in line.lower():
                order_id=line.split('#')
                clean_order_id=order_id[1].removesuffix(' has been created!')
                print(clean_order_id)
            if "store owner" in line.lower():
                # Using the page-level locator to perform the click
                self.page.get_by_text("store owner", exact=True).click()
                break
            
        time.sleep(4)

        # 5. Wait for the new page and return the header text
        contact_header = self.page.locator(".maintext")
        contact_header.wait_for(state="visible")
        print(contact_header.text_content().strip())
        
        return contact_header.text_content().strip()
        
                 
        # list1=[]
        # list1.append({'order_id':k})
        # df=pd.DataFrame(list1)
        # df.to_excel("test_results1.xlsx", index=False)

    print("Data exported successfully!")

    def click_back(self):
        self.page.locator("a").filter(has_text="Back").first.click()
        header=self.page.locator("h1.heading1").text_content().strip()
        time.sleep(3)
        print(header)
        return header
    

    

        

    
    

                    



