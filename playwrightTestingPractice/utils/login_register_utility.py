class LoginRegister:

    def __init__(self,page):
        self.page=page

    def navigation(self):
        self.page.goto("https://automationteststore.com/")

    def click_login_register_button(self):
        self.page.get_by_role("link", name="Login or register").click()