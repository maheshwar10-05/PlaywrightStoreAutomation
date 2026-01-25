
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
        return header_page

