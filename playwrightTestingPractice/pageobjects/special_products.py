
class SpecialProducts:

    def __init__(self,page):
        self.page=page

    def products_special(self):
        list_special=[]
        products=self.page.locator("a.prdocutname:visible")
        print(products.count())
        for i in range(products.count()):
            individual_product=products.nth(i).text_content().strip()
            list_special.append(individual_product)
        print(list_special)
        
    def click_absolue_eye(self):
        self.page.get_by_title("Absolue Eye Precious Cells").click()
        header_page=self.page.locator(".bgnone").text_content().strip()
        print(f"the header of the page is {header_page}")
        return header_page
    
    def click_ck_one_summer(self):
        self.page.get_by_title("ck one Summer 3.4 oz", exact=True).click()
        header_page=self.page.locator(".bgnone").text_content().strip()
        print(f"the header of the page is {header_page}")
        return header_page
    
    def click_replenishing_lipcolor(self):
        self.page.get_by_title("LE ROUGE ABSOLU Reshaping & Replenishing LipColour SPF 15", exact=True).click()
        header_page=self.page.locator(".bgnone").text_content().strip()
        print(f"the header of the page is {header_page}")
        return header_page
        
    def click_creme_nuit(self):
        self.page.get_by_title("Creme Precieuse Nuit 50ml").click()
        header_page=self.page.locator(".bgnone").text_content().strip()
        print(f"the header of the page is {header_page}")
        return header_page
        
        
        
    

