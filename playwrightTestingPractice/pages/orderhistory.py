import openpyxl
import re
import asyncio
import pandas as pd
from playwrightTestingPractice.config.config import EXCEL_FILE
from playwright.async_api import Page

class Orderhistory:

    def __init__(self, page: Page) -> None:
        self.page = page
        
        # --- LOCATORS ---
        self.order_id_label = self.page.locator("b").filter(has_text="Order ID:").first
        self.specific_order_id = self.page.locator(":text('Order ID: #69033')")
        self.main_header = self.page.locator("span.maintext")
        self.products_quantity_col = self.page.locator("//tbody/tr[2]/td[1]")
        self.total_price_elements = self.page.locator("//td[contains(text(), 'Total:')]")
        self.date_added_elements = self.page.locator("//div[@class='content']//table//td[contains(text(), 'Date Added:')]")
        self.status_elements = self.page.locator("//div[@class='container-fluid mt20']/div[2]")

    async def validate_excel_data(self):
        print("Excel Path:", EXCEL_FILE)
        # openpyxl is sync, which is fine here
        workbook = openpyxl.load_workbook(EXCEL_FILE)
        sheet = workbook.active
        expected_products = [cell.value for cell in sheet['A'] if cell.row > 1 and cell.value is not None]
        
        # Await Playwright actions
        order_id_text = await self.order_id_label.text_content()
        specific_id_text = await self.specific_order_id.text_content()
        
        y = specific_id_text.strip().split()
        id_num = 0
        for word in y:
            if word == "#69033":
                id_num = int(word.removeprefix("#"))

        for i, excel_val in enumerate(expected_products):
            if int(excel_val) == id_num:
                # Use f-string inside a locator call
                await self.page.locator(f"(//button[@title='View'][normalize-space()='View'])[{i+1}]").click()
        
        await self.page.wait_for_timeout(4000)
        result_text = await self.main_header.text_content()
        return result_text.strip() if result_text else ""
    
    async def excel_products_quantity_view(self):
        workbook = openpyxl.load_workbook(EXCEL_FILE)
        sheet = workbook.active
        expected_products = [cell.value for cell in sheet['B'] if cell.row > 1 and cell.value is not None]
        
        count_elements = await self.products_quantity_col.count()
        y = ""
        for i in range(count_elements):
            x = await self.products_quantity_col.nth(i).text_content()
            y = x.strip().removeprefix("Products: ")
            
        count = 0
        for j, excel_val in enumerate(expected_products):
            if y.isdigit() and int(y) == excel_val and excel_val == 2:
                await self.page.locator(f"(//button[@title='View'][normalize-space()='View'])[{j+1}]").click()
                await self.page.go_back()
                count += 1

        print(f"The number of orders with product quantity as 2: {count}")

    async def export_total_excel(self):
        df = pd.read_excel(EXCEL_FILE)
        num_rows_in_excel = len(df) 
        
        # Await the count of elements on the page
        web_count = await self.total_price_elements.count()
        
        for i in range(num_rows_in_excel):
            if i < web_count:
                total_text = await self.total_price_elements.nth(i).text_content()
                clean_price = total_text.strip().replace("Total: ", "").strip()
                df.at[i, 'Total'] = clean_price
                print(f"Updating Row {i+2} with {clean_price}")

        try:
            df.to_excel(EXCEL_FILE, index=False)
            print("Excel updated successfully.")
        except PermissionError:
            print("Error: Close the Excel file before running!")

    async def date_export_excel(self):
        df = pd.read_excel(EXCEL_FILE)
        web_count = await self.date_added_elements.count()
        
        for i in range(web_count):
            date_text = await self.date_added_elements.nth(i).text_content()
            clean_date = date_text.strip().removeprefix("Date Added: ")
            df.at[i, 'Date Added'] = clean_date
            print(f"Row {i} updated with: {clean_date}")

        try:
            df.to_excel(EXCEL_FILE, index=False)
        except PermissionError:
            print("Close the Excel file and try again!")

    async def status_excel(self):
        df = pd.read_excel(EXCEL_FILE)
        web_count = await self.status_elements.count()
        
        for i in range(web_count):
            status_text = await self.status_elements.nth(i).text_content()
            clean_status = status_text.strip().removeprefix("Status: ")
            df.at[i, 'Status'] = clean_status
            print(f"Row {i} updated with: {clean_status}")

        try:
            df.to_excel(EXCEL_FILE, index=False)
        except PermissionError:
            print("Close the Excel file and try again!")
