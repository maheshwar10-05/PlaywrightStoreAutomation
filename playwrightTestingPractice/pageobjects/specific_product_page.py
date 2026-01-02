import time
class Specificproduct:


    def __init__(self,page):
        self.page=page

    def product_specific(self):
        price_dict={}
        heading3=self.page.locator(".bgnone").text_content()
        print(heading3)
        self.page.locator("#product_quantity").clear()
        self.page.locator("#product_quantity").fill("4")
        self.page.locator("//div[@class='productfilneprice']").click()
        self.page.get_by_role("link",name="Add to Cart").click()
        self.page.go_back()
        time.sleep(4)
        price_key=self.page.locator("//label[@class='control-label']").first.text_content().strip().removesuffix(":\xa0\xa0\n\t\t\t\t\t\t\t\t\t\t\t$150.00")
        price_value=self.page.locator('span.total-price').text_content()
        price_dict[price_key]=price_value
        self.page.get_by_role("link",name="Print").click()
        self.page.pdf(path="playwrightTesting\output\playwrightproduct_page.pdf", format="A4")
        time.sleep(8)
        print(price_dict)

    def add_review_specific(self):
        price_dict={}
        heading3=self.page.locator(".bgnone").text_content()
        print(heading3)
        self.page.locator("#product_quantity").clear()
        self.page.locator("#product_quantity").fill("4")
        self.page.locator("//div[@class='productfilneprice']").click()
        self.page.get_by_role("link",name="Add to Cart").click()

       
        
    


        
    