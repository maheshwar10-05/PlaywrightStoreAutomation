import time
class Shoppingcart:

    def __init__(self,page):
        self.page=page

    def shopping(self):
        details={}
        table_headings=self.page.locator("//tbody/tr/th")
        for i in range(table_headings.count()):
            if table_headings.nth(i).filter(has_text="Name").count()>0:
                index=i
                print(index)
            elif table_headings.nth(i).filter(has_text="Model").count()>0:
                 index1=i
                 print(index1) 
            
        name_list=[]
        model_list=[]
        rows = self.page.locator("//div[@class='container-fluid cart-info product-list']/table/tbody/tr[td]")
    

        # 3. Iterate cleanly
        for i in range(rows.count()):
            # A. Capture the current row
            current_row = rows.nth(i)
            # B. CRITICAL FIX: 
            # Select the specific cell using the 'index' first.
            # This ensures we are always looking at the "Name" column, 
            # regardless of what classes other columns have.
            name_cell = current_row.locator("td").nth(index)
            # C. Extract the text from the anchor tag inside that specific cell
            product_name = name_cell.locator("a").text_content().strip()
            name_list.append(product_name)
            model_cell=current_row.locator("td").nth(index1)
            model_name=model_cell.text_content().strip()
            model_list.append(model_name)
           
        details["Name"]=name_list
        details["Model"]=model_list
        print(details)

    def apply_coupon(self):
        self.page.locator("#coupon_coupon").fill("ABCD123")
        self.page.locator("#apply_coupon_btn").click()
        error_message=self.page.locator("//div[@class='alert alert-error alert-danger']/strong").text_content().strip()
        return error_message
    def remove_coupon(self):
        self.page.locator("#remove_coupon_btn").click()
        remove_message=self.page.locator(".alert.alert-success").text_content().strip()
        return remove_message
    
    def estimate_shipping(self):
        self.page.locator('#estimate_country').select_option("India")
        time.sleep(2)
        self.page.locator('#estimate_country_zones').select_option("Goa")
        time.sleep(2)
        self.page.locator("#estimate_postcode").fill("502456")
        self.page.get_by_title("Estimate").click()
        x=self.page.locator("#shippings").text_content().strip()
        print(x)


    def remove_product_from_cart(self):
        rows = self.page.locator("//div[@class='container-fluid cart-info product-list']/table/tbody/tr[td]")
        for i in range(rows.count()):
            current_row = rows.nth(i)
            if current_row.locator("td").locator("a").filter(has_text="Designer Men Casual Formal Double Cuffs Grandad Band Collar Shirt Elegant Tie"):
               current_row.locator("td").locator("a.btn.btn-sm.btn-default").click()
               break
        time.sleep(3)

    def extract_shopping_cart_details(self):
        details={}
        table_headings=self.page.locator("//div[@class='container-fluid cart-info product-list']/table/tbody/tr/th")
        headings_list=[]
        for i in range(table_headings.count()):
            headers=table_headings.nth(i).text_content().strip()
            headings_list.append(headers)
        print(f"Headings found: {headings_list}")
        
        rows = self.page.locator("//div[@class='container-fluid cart-info product-list']/table/tbody/tr[td]")
    
        for i in range(rows.count()):
            model_dict={}
            quantity_dict={}
            unit_price_dict={}
            total_dict={}
            current_row = rows.nth(i)
            for index,header in enumerate(headings_list):
                 if header=="Name":
                      name_cell = current_row.locator("td").nth(index)
                      product_name = name_cell.locator("a").text_content().strip()
                     
                 elif header =="Model":
                     model_value = current_row.locator("td").nth(index).text_content().strip()
                     model_dict[header]=model_value
                 elif header =="Unit Price":
                     unit_value = current_row.locator("td").nth(index).text_content().strip()
                     unit_price_dict[header]=unit_value
                 elif header =="Total":
                     total_value = current_row.locator("td").nth(index).text_content().strip()
                     total_dict[header]=total_value
                     
                 elif header=="Quantity":
                     quantity_cell=current_row.locator("td").nth(index)
                     quantity_name=quantity_cell.locator("//div[@class='input-group input-group-sm']/input").input_value()
                     quantity_dict[header]=quantity_name
                     details[product_name]=model_dict,quantity_dict
                     
        print(details)
        return details
    def update_quantity_calculate(self):
        target_product = "Flash Bronzer Body Gel"
        rows = self.page.locator("//div[@class='container-fluid cart-info product-list']/table/tbody/tr[td]")
        
        for i in range(rows.count()):
            current_row = rows.nth(i)
            
            # 2. Check if THIS row contains the product name
            # We use .count() > 0 to get a True/False result
            if current_row.locator("td").locator("a").filter(has_text=target_product).count() > 0:
                
                print(f"Found '{target_product}' at row index {i}")
                
                # 3. Perform the action on THIS row's input
                # Note: We use 'current_row' here, not 'rows.nth(i)' repeatedly
                input_box = current_row.locator("td").locator("div").locator("input") # Adjust locator if nested (e.g., "div input")
                
                input_box.clear()
                input_box.fill("6")

                
                # 4. Stop the loop once found
                break
            
        self.page.get_by_role("button", name="Update").click()

        table_headings=self.page.locator("//div[@class='container-fluid cart-info product-list']/table/tbody/tr/th")
        headings_list=[]
        for i in range(table_headings.count()):
            headers=table_headings.nth(i).text_content().strip()
            headings_list.append(headers)
        rows = self.page.locator("//div[@class='container-fluid cart-info product-list']/table/tbody/tr[td]")
        
        for i in range(rows.count()):
            current_row = rows.nth(i)
            if current_row.locator("td").locator("a").filter(has_text=target_product).count() > 0:
                for index,header in enumerate(headings_list):
                    if header == "Unit Price":
                        unit_price=current_row.locator("td").nth(index).text_content().strip().split("$")
                        print(unit_price)
                        up=unit_price[1]
                        print(up)
                        
                    elif header =="Total":
                        total=current_row.locator("td").nth(index).text_content().strip()
                        print(total)
                    elif header =="Quantity":
                        quantity=current_row.locator("td").locator("div").locator("input").input_value()
                        print(quantity)
        calculate=float(up)*int(quantity)
        calculate1=f"${calculate}"
        print(calculate1)
        return total,calculate1

    def consolidated_total(self):
        rows = self.page.locator("//div[@class='container-fluid cart-info product-list']/table/tbody/tr[td]")
        headings_list=[]
        table_headings=self.page.locator("//div[@class='container-fluid cart-info product-list']/table/tbody/tr/th")
        for i in range(table_headings.count()):
            headers=table_headings.nth(i).text_content().strip()
            headings_list.append(headers)
        print(f"Headings found: {headings_list}")
        value_list=[]
        for i in range(rows.count()):
            
            current_row = rows.nth(i)
            for index,header in enumerate(headings_list):
                if header=="Total":
                    value=current_row.locator("td").nth(index).text_content().strip().split("$")
                    value_list.append(value[1])
        cal_total=sum(float(i) for i in value_list)
        ui_total=self.page.locator("//table[@id='totals_table']/tbody/tr[3]/td").last.text_content().strip()
        ship_rate=self.page.locator("//table[@id='totals_table']/tbody/tr[2]/td").last.text_content().strip().split('$')
        consolidated_amount=cal_total+float(ship_rate[1])
        x=f'${consolidated_amount}'
        print(x)
        print(ui_total)
        print(value_list)
        return ui_total,x
    
    def click_checkout(self):
        self.page.locator("#cart_checkout2").click()
        
    


        



            
             

        

    
    


              
              
                  
    
        
                

                
        



        

            
        

        