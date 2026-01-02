


class Login:
    def __init__(self, page):
        self.page = page

    
    def login(self,user_email,user_password):
        header3 = self.page.locator("h4[class='heading4']").last.text_content().strip()
        self.page.locator("#loginFrm_loginname").fill(user_email)
        self.page.locator("#loginFrm_password").fill(user_password) 
        screenshot_path=f"playwrightTesting/output/screenshots/test_login_page.png"
        screenshot_path1=f"playwrightTesting/output/screenshots/test_login_page2.png"
        self.page.screenshot(path=screenshot_path,full_page=True)
        self.page.screenshot(path=screenshot_path1,full_page=True)
        self.page.get_by_role("button",name="Login").click()
        return header3

    def login_verification(self):
        login_name=self.page.locator("div[class='menu_text']").text_content().strip()
        return login_name

    def click_home(self):
        self.page.locator('a').filter(has_text="Home").first.click()
        cart_count = self.page.locator("//a[@class='dropdown-toggle']/span[@class='label label-orange font14']").text_content()
        return cart_count.strip()

