import json

class Register:

    def __init__(self,page):
        self.page=page

    def account_login_page(self):
        header=self.page.locator(".maintext").text_content().strip()
        self.page.get_by_role("button", name="Continue").click()
        return header
    def enter_details_to_create_account(self,userdetails):
        header1=self.page.locator(".heading1").text_content().strip()
        self.page.locator("#AccountFrm_firstname").fill(userdetails["Firstname"])
        self.page.locator("#AccountFrm_lastname").fill(userdetails["Lastname"])
        self.page.locator("#AccountFrm_email").fill(userdetails["Email"])
        self.page.locator("#AccountFrm_address_1").fill(userdetails["Address1"])
        self.page.locator("#AccountFrm_city").fill(userdetails["city"])
        self.page.locator("#AccountFrm_country_id").select_option(userdetails["country"])
        self.page.locator("#AccountFrm_postcode").fill(userdetails["zip code"])
        self.page.locator("#AccountFrm_zone_id").select_option(userdetails["Region"])
        self.page.locator("#AccountFrm_loginname").fill(userdetails["Login name"])
        self.page.locator("#AccountFrm_password").fill(userdetails["Password"])
        self.page.locator("#AccountFrm_confirm").fill(userdetails["confirm password"])
        self.page.get_by_role("checkbox").click()
        self.page.get_by_role("button",name="Continue").click()
        header2=self.page.locator(".maintext").text_content().strip()
        print(header1,header2)
        return header1,header2







