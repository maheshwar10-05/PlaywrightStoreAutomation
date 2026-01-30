import time
class Subaccessory:
    def __init__(self,page):
        self.page=page

    def view_product(self):
        
        fragrance_sub=self.page.locator("//div[@class='col-md-3 col-sm-6 col-xs-12']/div[1]/div/a")
        for i in range(fragrance_sub.count()):
             if fragrance_sub.nth(i).filter(has_text="MAN Eau de Toilette Spray").count()>0:
                index=i
                print(index)
                if index<4:
                 self.page.locator(f"//div[@class='thumbnails grid row list-inline']//div[{index+1}]//div[2]//a[1]//img[1]").hover()
                 self.page.locator(f"//div[@class='thumbnails grid row list-inline']//div[{index+1}]//div[2]//div[1]//a[1]").click()
                else:
                    self.page.locator(f"//div[@class='thumbnails grid row list-inline']//div[{index+2}]//div[2]//a[1]//img[1]").hover()
                    self.page.locator(f"//div[@class='thumbnails grid row list-inline']//div[{index+2}]//div[2]//div[1]//a[1]").click()
    
            
        
    
            
                

        time.sleep(3)
        
        