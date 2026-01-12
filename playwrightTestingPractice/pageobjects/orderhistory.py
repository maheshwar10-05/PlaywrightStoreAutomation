import openpyxl,re
import pandas as pd
import time
class Orderhistory:


    def __init__(self,page) -> None:
        self.page=page

    def validate_excel_data(self):
    # 1. Read data from Excel
        path = "C:/Users/2148389/PycharmProjects/PlaywrightStoreAutomation/playwrightTestingPractice/testcases/test_results1.xlsx"
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        # Assuming cell A2 contains the expected product name
        expected_products = [cell.value for cell in sheet['A'] if cell.row > 1 and cell.value is not None]
        
        print(f"Expected value from Excel: {expected_products}")
        x=self.page.locator("b").filter(has_text="Order ID:").first.text_content().strip()
        y=self.page.locator(":text('Order ID: #68564')").text_content().strip().split()
        id_string=""
        for word in y:
            if word=="#68564":
                id_string=word
                id_num=int(id_string.removeprefix("#"))
        for i,excel_val in enumerate(expected_products):
            if int(excel_val)==id_num:
                    self.page.locator(f"(//button[@title='View'][normalize-space()='View'])[{i+1}]").click()
        time.sleep(4)
        result_page=self.page.locator("span.maintext").text_content().strip()
        print(result_page)
        return result_page
    
    def excel_products_quantity_view(self):
         products_quan=self.page.locator("//tbody/tr[2]/td[1]")
         path = "C:/Users/2148389/PycharmProjects/PlaywrightStoreAutomation/playwrightTestingPractice/testcases/test_results1 (version 1).xlsb.xlsx"
         workbook = openpyxl.load_workbook(path)
         sheet = workbook.active
        # Assuming cell A2 contains the expected product name
         expected_products = [cell.value for cell in sheet['B'] if cell.row > 1 and cell.value is not None]
         for i in range(products_quan.count()):
              x=products_quan.nth(i).text_content().strip()
              
              y=x.removeprefix("Products: ")
              print(y)
         count=0
         for j,excel_val in enumerate(expected_products):
              if int(y)==excel_val and excel_val==2:
               
               self.page.locator(f"(//button[@title='View'][normalize-space()='View'])[{j+1}]").click()
               self.page.go_back()
               count=count+1
         
               

         print(f"The number of orders with product quantity as 2 :{count}")


    def export_total_excel(self):
        path = "C:/Users/2148389/PycharmProjects/PlaywrightStoreAutomation/playwrightTestingPractice/testcases/test_results1.xlsx"
        df = pd.read_excel(path)
        
        # Target ONLY the price elements in the table
        total_price_locator = self.page.locator("//td[contains(text(), 'Total:')]")
        
        # Use the number of rows in your Excel to stop the loop early
        num_rows_in_excel = len(df) 
        
        for i in range(num_rows_in_excel):
            # Safety check: make sure the website actually has the element
            if i < total_price_locator.count():
                total_text = total_price_locator.nth(i).text_content().strip()
                
                # Clean the text to get "$120.50"
                clean_price = total_text.replace("Total: ", "").strip()
                
                # Assign to the specific row index
                df.at[i, 'Total'] = clean_price
                print(f"Updating Row {i+2} with {clean_price}")

        try:
            df.to_excel(path, index=False)
            print("Excel updated successfully without extra repeated rows.")
        except PermissionError:
            print("Error: Close the Excel file before running!")
            # Use RegEx to see if the text contains a number
            # This prevents the 'Jasmin Noir' string from crashing the script
                # match = re.search(r"(\d+\.?\d*)", total_text)
                # if match:
                #     final_price = float(match.group(1))
                #     print(f"Found valid price: {final_price}")
                    # Exit loop once we find the price


                


    def date_export_excel(self):
        path = "C:/Users/2148389/PycharmProjects/PlaywrightStoreAutomation/playwrightTestingPractice/testcases/test_results1.xlsx"
        df = pd.read_excel(path)
        number_excel_rows=len(df)
        date_info=self.page.locator("//div[@class='content']//table//td[contains(text(), 'Date Added:')]")
        for i in range(date_info.count()):
    
            date_text=date_info.nth(i).text_content().strip()
            print(date_text)
        # Use RegEx to see if the text contains a number
        # This prevents the 'Jasmin Noir' string from crashing the script
            # match = re.search(r"(\d+\.?\d*)", total_text)
            # if match:
            #     final_price = float(match.group(1))
            #     print(f"Found valid price: {final_price}")
                 # Exit loop once we find the price

    # 3. Assign to the 'Total' column and save
            
            clean_date= date_text.removeprefix("Date Added: ")
            df.at[i, 'Date Added'] = clean_date
            print(f"Row {i} updated with: {clean_date}")

        try:
          df.to_excel(path, index=False)
          print("Excel updated successfully with all individual prices.")
        except PermissionError:
          print("Close the Excel file and try again!")

    def status_excel(self):
        path = "C:/Users/2148389/PycharmProjects/PlaywrightStoreAutomation/playwrightTestingPractice/testcases/test_results1.xlsx"
        df = pd.read_excel(path)
        number_excel_rows=len(df)
        status_info=self.page.locator("//div[@class='container-fluid mt20']/div[2]")
        for i in range(status_info.count()):
    
            status_text=status_info.nth(i).text_content().strip()
            print(status_text)
        # Use RegEx to see if the text contains a number
        # This prevents the 'Jasmin Noir' string from crashing the script
            # match = re.search(r"(\d+\.?\d*)", total_text)
            # if match:
            #     final_price = float(match.group(1))
            #     print(f"Found valid price: {final_price}")
                 # Exit loop once we find the price

    # 3. Assign to the 'Total' column and save
            
            clean_status= status_text.removeprefix("Status: ")
            df.at[i, 'Status'] = clean_status
            print(f"Row {i} updated with: {clean_status}")

        try:
          df.to_excel(path, index=False)
          print("Excel updated successfully with all individual prices.")
        except PermissionError:
          print("Close the Excel file and try again!")

    
              
         



              

    

    


        



        