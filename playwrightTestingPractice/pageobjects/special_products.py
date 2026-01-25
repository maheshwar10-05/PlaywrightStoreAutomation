
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
    
    def input_quantity_special(self):
        self.page.locator("#product_quantity").clear()
        self.page.locator("#product_quantity").fill("3")
        updated_quantity=self.page.locator("#product_quantity").input_value().strip()
        print(f"The updated quantity is {updated_quantity}")
        total_price=self.page.locator("label.control-label:visible").text_content().strip()
        list_price=[]
        list_price.append(total_price)
        update_list_price=list_price[0].replace("\xa0\xa0\n\t\t\t\t\t\t\t\t\t\t\t","").strip().split("$")
        update_list_price.pop(0)
        int_price=float(update_list_price[0])
        single_price=self.page.locator("div.productfilneprice").text_content().strip().split("$")
        single_price.pop(0)
        single_float_price=float(single_price[0])
        print(f"The price of the products {int_price}")
        print(f"The single price of the product {single_float_price}")
        
        return int_price,single_float_price,updated_quantity

