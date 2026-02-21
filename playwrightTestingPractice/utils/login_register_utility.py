from playwrightTestingPractice.pages.login import Login
from playwrightTestingPractice.pages.homepage import Homepage
from playwrightTestingPractice.utils.utility import user_credentials2
class LoginRegister:

    def __init__(self,page):
        self.page=page

    def click_login_register_button(self):
        self.page.get_by_role("link", name="Login or register").click()
        
    
        