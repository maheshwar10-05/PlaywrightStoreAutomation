import openpyxl,time


class Login:
    def __init__(self, page):
        self.page = page
        self.user_input=page.locator("#loginFrm_loginname")
        self.pass_input=page.locator("#loginFrm_password")
        self.header_text=page.locator("h4[class='heading4']").last
        self.login_button=page.get_by_role("button",name="Login")
        self.user_name_after_login=page.locator("div[class='menu_text']")
        self.home_link=page.locator('a').filter(has_text="Home").first
        self.cart_count_text=page.locator("//a[@class='dropdown-toggle']/span[@class='label label-orange font14']")
        self.error_message=page.locator("div.alert.alert-error.alert-danger")
        self.url_stable=page.wait_for_load_state("networkidle")
        self.login_name=page.locator("div.menu_text")
        self.forgot_login_link=page.get_by_role("link", name="Forgot your login?")
        self.forgot_header_page_text=page.locator("span.maintext")
        self.forgot_last_name_input=page.locator("#forgottenFrm_lastname")
        self.forgot_email_input=page.locator("#forgottenFrm_email")
        self.click_continue=page.get_by_role("button", name="Continue")
        self.alert_success=page.locator("div.alert.alert-success")
    
    async def login(self,user_credentials2):
        await self.user_input.fill(user_credentials2["Login name"])
        await self.pass_input.fill(user_credentials2["Password"]) 
        # screenshot_path=f"playwrightTesting/output/screenshots/test_login_page.png"
        # screenshot_path1=f"playwrightTesting/output/screenshots/test_login_page2.png"
        # self.page.screenshot(path=screenshot_path,full_page=True)
        # self.page.screenshot(path=screenshot_path1,full_page=True)
        await self.login_button.click()
        return (await self.header_text.text_content()).strip()
    
    async def correct_login_details_check(self,user_email,user_password):
        
        await self.user_input.fill(user_email)
        await self.pass_input.fill(user_password) 
        await self.login_button.click()
        return (await self.login_name.text_content()).strip()

    async def login_verification(self):
        return (await self.user_name_after_login.text_content()).strip()

    async def click_home(self):
        await self.home_link.click()
        return (await self.cart_count_text.text_content()).strip()
    
    async def enter_incorrect_login_details(self,incorrect_login_details):
        await self.user_input.fill(incorrect_login_details["username"])
        await self.pass_input.fill(incorrect_login_details["password"]) 
        await self.login_button.click()
        print((await self.error_message.text_content()).strip())
        return (await self.error_message.text_content()).strip()
    
    async def enter_correct_login_name_incorrect_password(self,login_correct_incorrect_password):
        
        await self.user_input.fill(login_correct_incorrect_password["username"])
        await self.pass_input.fill(login_correct_incorrect_password["password"]) 
        await self.login_button.click()
        print((await self.error_message.text_content()).strip())
        return (await self.error_message.text_content()).strip()

    async def enter_incorrect_login_correct_password(self,incorrect_login_correct_password):
        await self.user_input.fill(incorrect_login_correct_password["username"])
        await self.pass_input.fill(incorrect_login_correct_password["password"]) 
        await self.login_button.click()
        print((await self.error_message.text_content()).strip())
        return (await self.error_message.text_content()).strip()
    
    async def enter_correct_login_empty_password(self,login_correct_empty_password):
        await self.user_input.fill(login_correct_empty_password["username"])
        await self.pass_input.fill(login_correct_empty_password["password"]) 
        await self.login_button.click()
        print((await self.error_message.text_content()).strip())
        return (await self.error_message.text_content()).strip()
    
    async def enter_empty_login_correct_password(self,empty_login_correct_password):
        await self.user_input.fill(empty_login_correct_password["username"])
        await self.pass_input.fill(empty_login_correct_password["password"]) 
        await self.login_button.click()
        print((await self.error_message.text_content()).strip())
        return (await self.error_message.text_content()).strip()
    
    async def enter_empty_login_empty_password(self,empty_login_empty_password):
        await self.user_input.fill(empty_login_empty_password["username"])
        await self.pass_input.fill(empty_login_empty_password["password"]) 
        await self.login_button.click()
        print((await self.error_message.text_content()).strip())
        return (await self.error_message.text_content()).strip()

    async def excel_data_login_password(self, user_name, user_password):
        # username
        # If user_name is None, we send "", which effectively clears the field
        await self.user_input.fill(user_name if user_name is not None else "")

        # password
        await self.pass_input.fill(user_password if user_password is not None else "")

        await self.login_button.click()

        await self.url_stable

        # 1. Wait for either the success or error message to appear
        # We use a locator that covers both, or wait for one specifically
        try:
            # Wait for either to be attached to the DOM
            await self.error_message.wait_for(state="visible", timeout=5000)
        except:
            # If error doesn't show, maybe success did?
            pass

        # 2. Now check visibility
        if await self.error_message.is_visible():
            text = await self.error_message.text_content()
            return None, text.strip()

        if await self.alert_success.is_visible():
            text = await self.login_name.text_content()
            return text.strip(), None

        return None, "Unexpected state"
    
    
    
    async def forgot_login(self,last_name,email):
        await self.forgot_login_link.click()
        header=self.forgot_header_page_text.text_content()
        
        # last_name
        # If last_name is None, it fills "", otherwise it fills the actual name
        await self.forgot_last_name_input.fill(last_name if last_name is not None else "")
        # email
        # If email is None, it fills "", otherwise it fills the email
        await self.forgot_email_input.fill(email if email is not None else "")
        await self.click_continue.click()
        await self.url_stable
        
# 1. Use a locator that represents "any message appeared" 
# or wait for a specific one with a short timeout.
        try:
            # Wait up to 5 seconds for the success message to show up
            await self.alert_success.wait_for(state="visible", timeout=5000)
        except:
            # If success doesn't show, we assume it might be an error or just slow
            pass

        # 2. Check for Success (Must use 'await' here)
        if await self.alert_success.is_visible():
            success_header = (await self.alert_success.text_content()).strip()
            return success_header, None

        # 3. Check for Failure (Must use 'await' here)
        if await self.error_message.is_visible():
            error_header = (await self.error_message.text_content()).strip()
            return error_header,None  # Returning (None, error) matches standard patterns

        return None, "No message detected"
                
                
        
        

        
        
            
        
        