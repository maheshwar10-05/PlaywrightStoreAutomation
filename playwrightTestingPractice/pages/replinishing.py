from playwright.async_api import expect
class Replinishing:
    
    def __init__(self,page):
        self.page=page
        self.timeout=page.wait_for_timeout(5000)
        self.qty_input = self.page.locator("#product_quantity")
        self.total_price_label = self.page.locator("span.total-price")
        self.single_price_div = self.page.locator("div.productfilneprice")
        self.add_to_cart_btn = self.page.get_by_role("link", name="Add to Cart")
        self.main_header = self.page.locator("span.maintext")
        self.model_number_item = self.page.locator("//div[@class='tab-content']//li[1]")
        self.brand_link = self.page.locator("//ul[@class='productinfo']//li//a")
    
    async def input_quantity_special_replinishing(self):
        # 1. Update Quantity
        await self.qty_input.clear()
        await self.qty_input.fill("3")
        
        # 2. Extract and clean the updated quantity
        updated_quantity_val = await self.qty_input.input_value()
        updated_quantity = updated_quantity_val.strip()
        print(f"The updated quantity is {updated_quantity}")
        await self.timeout
        # 3. Extract and clean Total Price from label (e.g., "Total:  $120.00"
        total_price_text = self.total_price_label
        # Cleaning out the special characters and splitss
        clean_total = (await total_price_text.text_content()).strip()
    
    
        # Split by $ and take the second part
        int_price = float(clean_total.split("$")[1])
        
        # 4. Extract and clean Single Price (e.g., "$40.00")
        single_price_text = (await self.single_price_div.text_content())
        single_float_price = float(single_price_text.strip().replace("$", ""))
        
        print(f"The calculated total price: {clean_total}")
        print(f"The single price: {single_float_price}")
        
        return int_price, single_float_price, updated_quantity
    
    async def click_add_cart_replinishing(self):
        await self.add_to_cart_btn.click()
        # Await the text content of the header on the next page
        header_text = await self.main_header.text_content()
        target_page = header_text.strip() if header_text else ""
        print(target_page)
        return target_page

    async def extract_model_number_replinishing(self):
        model_text = await self.model_number_item.text_content()
        model_number = model_text.strip() if model_text else ""
        print(model_number)
        return model_number
        
    async def click_lancome_brand(self):
        await self.brand_link.click()
        header_text = await self.main_header.text_content()
        header1 = header_text.strip() if header_text else ""
        print(header1)
        return header1