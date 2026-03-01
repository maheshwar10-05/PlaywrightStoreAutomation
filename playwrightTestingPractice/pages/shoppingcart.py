class Shoppingcart:

    def __init__(self,page):
        self.page = page
        
        # --- TABLE LOCATORS ---
        self.table_headings = self.page.locator("//div[@class='container-fluid cart-info product-list']/table/tbody/tr/th")
        self.cart_rows = self.page.locator("//div[@class='container-fluid cart-info product-list']/table/tbody/tr[td]")
        
        # --- COUPON LOCATORS ---
        self.coupon_input = self.page.locator("#coupon_coupon")
        self.apply_coupon_btn = self.page.locator("#apply_coupon_btn")
        self.remove_coupon_btn = self.page.locator("#remove_coupon_btn")
        self.coupon_error_msg = self.page.locator("//div[@class='alert alert-error alert-danger']/strong")
        self.coupon_success_msg = self.page.locator(".alert.alert-success")
        
        # --- SHIPPING LOCATORS ---
        self.estimate_country_select = self.page.locator('#estimate_country')
        self.estimate_zone_select = self.page.locator('#estimate_country_zones')
        self.postcode_input = self.page.locator("#estimate_postcode")
        self.estimate_btn = self.page.get_by_title("Estimate")
        self.shipping_result = self.page.locator("#shippings")
        
        # --- TOTALS TABLE ---
        self.totals_table_rows = self.page.locator("//table[@id='totals_table']/tbody/tr")
        self.checkout_btn = self.page.locator("#cart_checkout2")
        self.update_btn = self.page.get_by_role("button", name="Update")

    async def shopping(self):
        details = {}
        count = await self.table_headings.count()
        index = -1
        index1 = -1
        
        for i in range(count):
            heading = self.table_headings.nth(i)
            if await heading.filter(has_text="Name").count() > 0:
                index = i
            elif await heading.filter(has_text="Model").count() > 0:
                index1 = i
            
        name_list = []
        model_list = []
        row_count = await self.cart_rows.count()

        for i in range(row_count):
            current_row = self.cart_rows.nth(i)
            product_name = await current_row.locator("td").nth(index).locator("a").text_content()
            model_name = await current_row.locator("td").nth(index1).text_content()
            
            name_list.append(product_name.strip() if product_name else "")
            model_list.append(model_name.strip() if model_name else "")
            
        details["Name"] = name_list
        details["Model"] = model_list
        print(details)
        return details

    async def apply_coupon(self):
        await self.coupon_input.fill("ABCD123")
        await self.apply_coupon_btn.click()
        error_text = await self.coupon_error_msg.text_content()
        return error_text.strip() if error_text else ""

    async def remove_coupon(self):
        await self.remove_coupon_btn.click()
        msg = await self.coupon_success_msg.text_content()
        return msg.strip() if msg else ""
    
    async def estimate_shipping(self):
        await self.estimate_country_select.select_option("India")
        await self.page.wait_for_timeout(2000)
        await self.estimate_zone_select.select_option("Goa")
        await self.page.wait_for_timeout(2000)
        await self.postcode_input.fill("502456")
        await self.estimate_btn.click()
        result_text = await self.shipping_result.text_content()
        print(result_text.strip() if result_text else "")

    async def remove_product_from_cart(self):
        row_count = await self.cart_rows.count()
        target = "Designer Men Casual Formal Double Cuffs Grandad Band Collar Shirt Elegant Tie"
        for i in range(row_count):
            current_row = self.cart_rows.nth(i)
            if await current_row.locator("td").locator("a").filter(has_text=target).count() > 0:
                await current_row.locator("td").locator("a.btn.btn-sm.btn-default").click()
                break
        await self.page.wait_for_timeout(3000)

    async def extract_shopping_cart_details(self):
        details = {}
        headings_count = await self.table_headings.count()
        headings_list = []
        for i in range(headings_count):
            header = await self.table_headings.nth(i).text_content()
            headings_list.append(header.strip() if header else "")
        
        row_count = await self.cart_rows.count()
        for i in range(row_count):
            model_dict, quantity_dict, unit_price_dict, total_dict = {}, {}, {}, {}
            current_row = self.cart_rows.nth(i)
            product_name = ""
            
            for index, header in enumerate(headings_list):
                cell = current_row.locator("td").nth(index)
                if header == "Name":
                    product_name = (await cell.locator("a").text_content()).strip()
                elif header == "Model":
                    model_dict[header] = (await cell.text_content()).strip()
                elif header == "Unit Price":
                    unit_price_dict[header] = (await cell.text_content()).strip()
                elif header == "Total":
                    total_dict[header] = (await cell.text_content()).strip()
                elif header == "Quantity":
                    qty = await cell.locator("//div[@class='input-group input-group-sm']/input").input_value()
                    quantity_dict[header] = qty
            
            details[product_name] = (model_dict, quantity_dict)
        print(details)
        return details

    async def update_quantity_calculate(self):
        target_product = "Flash Bronzer Body Gel"
        row_count = await self.cart_rows.count()
        
        for i in range(row_count):
            current_row = self.cart_rows.nth(i)
            if await current_row.locator("td").locator("a").filter(has_text=target_product).count() > 0:
                input_box = current_row.locator("td").locator("div").locator("input")
                await input_box.clear()
                await input_box.fill("6")
                break
            
        await self.update_btn.click()

        headings_count = await self.table_headings.count()
        headings_list = [(await self.table_headings.nth(i).text_content()).strip() for i in range(headings_count)]
        
        unit_price, quantity, total = None, None, None

        for i in range(row_count):
            current_row = self.cart_rows.nth(i)
            if await current_row.locator("td").locator("a").filter(has_text=target_product).count() > 0:
                for index, header in enumerate(headings_list):
                    cell = current_row.locator("td").nth(index)
                    if header == "Unit Price":
                        unit_price = (await cell.text_content()).strip()
                    elif header == "Total":
                        total = (await cell.text_content()).strip()
                    elif header == "Quantity":
                        quantity = await cell.locator("div").locator("input").input_value()
                break

        unit_price_value = float(unit_price.replace("$", "").replace(",", ""))
        print(unit_price_value)
        calculate = unit_price_value * int(quantity)
        calculate_str = f"${calculate:.2f}"
        return total, calculate_str

    async def consolidated_total(self):
        row_count = await self.cart_rows.count()
        headings_count = await self.table_headings.count()
        headings_list = [(await self.table_headings.nth(i).text_content()).strip() for i in range(headings_count)]
        
        value_list = []
        for i in range(row_count):
            current_row = self.cart_rows.nth(i)
            for index, header in enumerate(headings_list):
                if header == "Total":
                    val = await current_row.locator("td").nth(index).text_content()
                    value_list.append(val.strip().replace("$", ""))
        
        cal_total = sum(float(i) for i in value_list)
        ui_total = await self.page.locator("//table[@id='totals_table']/tbody/tr[3]/td").last.text_content()
        ship_rate_raw = await self.page.locator("//table[@id='totals_table']/tbody/tr[2]/td").last.text_content()
        
        ship_rate = ship_rate_raw.strip().split('$')
        consolidated_amount = cal_total + float(ship_rate[1])
        result_str = f'${consolidated_amount}'
        
        return ui_total.strip().replace(",", ""), result_str
    
    async def click_checkout(self):
        await self.checkout_btn.click()