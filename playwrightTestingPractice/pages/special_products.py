class SpecialProducts:

    def __init__(self, page):
        self.page = page
        
        # --- LOCATORS ---
        self.special_products_list = self.page.locator("a.prdocutname:visible")
        self.page_header = self.page.locator(".bgnone")
        
        # Specific Product Locators
        self.absolue_eye_link = self.page.get_by_title("Absolue Eye Precious Cells")
        self.ck_one_summer_link = self.page.get_by_title("ck one Summer 3.4 oz", exact=True)
        self.replenishing_lipcolor_link = self.page.get_by_title(
            "LE ROUGE ABSOLU Reshaping & Replenishing LipColour SPF 15", exact=True
        )
        self.creme_nuit_link = self.page.get_by_title("Creme Precieuse Nuit 50ml")

    # --- METHODS ---

    async def products_special(self):
        list_special = []
        # Rule: await the count() call
        count = await self.special_products_list.count()
        print(count)
        
        # Original loop pattern
        for i in range(count):
            individual_product = await self.special_products_list.nth(i).text_content()
            list_special.append(individual_product.strip() if individual_product else "")
        
        print(list_special)
        return list_special
        
    async def click_absolue_eye(self):
        await self.absolue_eye_link.click()
        # Ensure text_content is awaited and then stripped
        header_text = await self.page_header.text_content()
        header_page = header_text.strip() if header_text else ""
        print(f"the header of the page is {header_page}")
        return header_page
    
    async def click_ck_one_summer(self):
        await self.ck_one_summer_link.click()
        header_text = await self.page_header.text_content()
        header_page = header_text.strip() if header_text else ""
        print(f"the header of the page is {header_page}")
        return header_page
    
    async def click_replenishing_lipcolor(self):
        await self.replenishing_lipcolor_link.click()
        header_text = await self.page_header.text_content()
        header_page = header_text.strip() if header_text else ""
        print(f"the header of the page is {header_page}")
        return header_page
        
    async def click_creme_nuit(self):
        await self.creme_nuit_link.click()
        header_text = await self.page_header.text_content()
        header_page = header_text.strip() if header_text else ""
        print(f"the header of the page is {header_page}")
        return header_page

    async def random_click(self):
        # Even if it's just an assertion, making it async maintains consistency
        assert True