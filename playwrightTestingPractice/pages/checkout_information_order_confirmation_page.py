import re
import asyncio
import pandas as pd


class Orderpage:
    def __init__(self, page):
        self.page = page
        
        # --- LOCATORS ---
        self.main_header = self.page.locator("span.maintext")
        self.return_policy_link = self.page.get_by_role("link", name="Return Policy")
        self.policy_paragraphs = self.page.locator("//div[@class='middle']/p")
        self.close_btn = self.page.get_by_text("Close")
        
        self.edit_shipping_link = self.page.get_by_role("link", name="Edit Shipping")
        self.edit_payment_link = self.page.get_by_role("link", name="Edit Payment")
        self.edit_cart_link = self.page.get_by_role("link", name="Edit Cart")
        
        self.confirm_order_btn = self.page.get_by_text("Confirm Order", exact=True)
        self.success_main_text = self.page.locator(".maintext")
        
        self.success_container = self.page.locator("section.mb40")
        self.success_paragraphs = self.success_container.locator("p")
        self.store_owner_link = self.page.get_by_text("store owner", exact=True)
        
        self.back_btn = self.page.locator("a").filter(has_text="Back")
        self.h1_heading = self.page.locator("h1.heading1")
        self.timeout=page.wait_for_timeout(5000)

    # --- METHODS ---

    async def order_confirmation_page(self):
        # Replacing wait_for_selector with locator-based waiting
        await self.main_header.first.wait_for(state="visible")
        await self.page.wait_for_timeout(5000)
        return await self.main_header.first.text_content()
    
    async def return_policy_popup(self):
        await self.return_policy_link.first.click()

    async def pop_up_text(self):
        policy_dict = {}
        # Await text content for first and last elements
        web_ele = await self.policy_paragraphs.first.text_content()
        web_ele2 = await self.policy_paragraphs.last.text_content()
        
        policy_dict[web_ele] = web_ele2
        print(policy_dict)
        await self.close_btn.first.click()

    async def edit_shipping(self):
        await self.timeout
        await self.edit_shipping_link.click()
        await self.timeout
        title_target_page = await self.main_header.text_content()
        await self.page.go_back()
        return title_target_page

    async def edit_payment(self):
        await self.edit_payment_link.click()
        title_target_page = await self.main_header.text_content()
        await self.page.go_back()
        return title_target_page

    async def edit_cart(self):
        await self.edit_cart_link.click()
        page_title = await self.main_header.text_content()
        return page_title
    
    async def click_confirm_order(self):
        await self.confirm_order_btn.click()
        await self.page.wait_for_timeout(5000)
        
        await self.success_main_text.wait_for(state="visible")
        success = await self.success_main_text.text_content()
        result = success.strip() if success else ""
        print(result)
        return result
    
    async def order_id(self):
        await self.success_container.wait_for(state="visible")

        # Get all paragraph locators and iterate to extract text
        paragraphs_locators = await self.success_paragraphs.all()
        order_list = []
        for p in paragraphs_locators:
            text = await p.text_content()
            order_list.append(text.strip() if text else "")
        
        print(f"Extracted Lines: {order_list}")

        for line in order_list:
            if "#" in line.lower():
                order_parts = line.split('#')
                clean_order_id = order_parts[1].removesuffix(' has been created!')
                print(f"Order ID: {clean_order_id}")
            
            if "store owner" in line.lower():
                await self.store_owner_link.click()
                break
            
        await self.page.wait_for_timeout(4000)

        await self.success_main_text.wait_for(state="visible")
        header_text = await self.success_main_text.text_content()
        final_text = header_text.strip() if header_text else ""
        print(final_text)
        
        return final_text

    async def click_back(self):
        await self.back_btn.first.click()
        header_raw = await self.h1_heading.text_content()
        header = header_raw.strip() if header_raw else ""
        await self.page.wait_for_timeout(3000)
        print(header)
        return header