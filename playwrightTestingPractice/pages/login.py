import openpyxl,time


class Login:
    def __init__(self, page):
        self.page = page

    
    def login(self,user_credentials2):
        header3 = self.page.locator("h4[class='heading4']").last.text_content().strip()
        self.page.locator("#loginFrm_loginname").fill(user_credentials2["Login name"])
        self.page.locator("#loginFrm_password").fill(user_credentials2["Password"]) 
        # screenshot_path=f"playwrightTesting/output/screenshots/test_login_page.png"
        # screenshot_path1=f"playwrightTesting/output/screenshots/test_login_page2.png"
        # self.page.screenshot(path=screenshot_path,full_page=True)
        # self.page.screenshot(path=screenshot_path1,full_page=True)
        self.page.get_by_role("button",name="Login").click()
        return header3
    
    def correct_login_details_check(self,user_email,user_password):
        header3 = self.page.locator("h4[class='heading4']").last.text_content().strip()
        self.page.locator("#loginFrm_loginname").fill(user_email)
        self.page.locator("#loginFrm_password").fill(user_password) 
        self.page.get_by_role("button",name="Login").click()
        return header3

    def login_verification(self):
        login_name=self.page.locator("div[class='menu_text']").text_content().strip()
        return login_name

    def click_home(self):
        self.page.locator('a').filter(has_text="Home").first.click()
        cart_count = self.page.locator("//a[@class='dropdown-toggle']/span[@class='label label-orange font14']").text_content()
        return cart_count.strip()
    
    def enter_incorrect_login_details(self,incorrect_login_details):
        self.page.locator("#loginFrm_loginname").fill(incorrect_login_details["username"])
        self.page.locator("#loginFrm_password").fill(incorrect_login_details["password"]) 
        self.page.get_by_role("button",name="Login").click()
        error_message=self.page.locator("div.alert.alert-error.alert-danger").text_content().strip()
        print(error_message)
        return error_message
    
    def enter_correct_login_name_incorrect_password(self,login_correct_incorrect_password):
        
        self.page.locator("#loginFrm_loginname").fill(login_correct_incorrect_password["username"])
        self.page.locator("#loginFrm_password").fill(login_correct_incorrect_password["password"]) 
        self.page.get_by_role("button",name="Login").click()
        error_message=self.page.locator("div.alert.alert-error.alert-danger").text_content().strip()
        print(error_message)
        return error_message

    def enter_incorrect_login_correct_password(self,incorrect_login_correct_password):
        self.page.locator("#loginFrm_loginname").fill(incorrect_login_correct_password["username"])
        self.page.locator("#loginFrm_password").fill(incorrect_login_correct_password["password"]) 
        self.page.get_by_role("button",name="Login").click()
        error_message=self.page.locator("div.alert.alert-error.alert-danger").text_content().strip()
        print(error_message)
        return error_message
    
    def enter_correct_login_empty_password(self,login_correct_empty_password):
        self.page.locator("#loginFrm_loginname").fill(login_correct_empty_password["username"])
        self.page.locator("#loginFrm_password").fill(login_correct_empty_password["password"]) 
        self.page.get_by_role("button",name="Login").click()
        error_message=self.page.locator("div.alert.alert-error.alert-danger").text_content().strip()
        print(error_message)
        return error_message
    
    def enter_empty_login_correct_password(self,empty_login_correct_password):
        self.page.locator("#loginFrm_loginname").fill(empty_login_correct_password["username"])
        self.page.locator("#loginFrm_password").fill(empty_login_correct_password["password"]) 
        self.page.get_by_role("button",name="Login").click()
        error_message=self.page.locator("div.alert.alert-error.alert-danger").text_content().strip()
        print(error_message)
        return error_message
    
    def enter_empty_login_empty_password(self,empty_login_empty_password):
        self.page.locator("#loginFrm_loginname").fill(empty_login_empty_password["username"])
        self.page.locator("#loginFrm_password").fill(empty_login_empty_password["password"]) 
        self.page.get_by_role("button",name="Login").click()
        error_message=self.page.locator("div.alert.alert-error.alert-danger").text_content().strip()
        print(error_message)
        return error_message

    def excel_data_login_password(self, user_name, user_password):

        # username
        if user_name is not None:
            self.page.locator("#loginFrm_loginname").fill(user_name)
        else:
            self.page.locator("#loginFrm_loginname").clear()

        # password
        if user_password is not None:
            self.page.locator("#loginFrm_password").fill(user_password)
        else:
            self.page.locator("#loginFrm_password").clear()

        self.page.locator("button[title='Login']").click()

        self.page.wait_for_load_state("networkidle")

        # Failure case (empty field / invalid login)
        if self.page.locator("div.alert.alert-error.alert-danger").is_visible():
            error_message = self.page.locator(
                "div.alert.alert-error.alert-danger"
            ).text_content().strip()
            return None, error_message

        # Success case
        if self.page.locator("div.menu_text").is_visible():
            login_name = self.page.locator(
                "div.menu_text"
            ).text_content().strip()
            return login_name, None

        return None, "Unexpected state"
    
    
    
    def forgot_login(self,last_name,email):
        self.page.get_by_role("link", name="Forgot your login?").click()
        header=self.page.locator("span.maintext").text_content()
        
        # last_name
        if last_name is not None:
            self.page.locator("#forgottenFrm_lastname").fill(last_name)
        else:
            self.page.locator("#forgottenFrm_lastname").clear()
        #email
        if email is not None:
            self.page.locator("#forgottenFrm_email").fill(email)
        else:
            self.page.locator("#forgottenFrm_email").clear()
            
            
            
        self.page.get_by_role("button", name="Continue").click()
        self.page.wait_for_load_state("networkidle")
        
        #success
        if self.page.locator("div.alert.alert-success").is_visible():
            
            success_header=self.page.locator("div.alert.alert-success").text_content().strip()
            
            return success_header,None
        #failure
        if self.page.locator("div.alert.alert-error.alert-danger").is_visible():
            error_header=self.page.locator("div.alert.alert-error.alert-danger").text_content().strip()
            return error_header,None
        
        
        
        

        
        
            
        
        