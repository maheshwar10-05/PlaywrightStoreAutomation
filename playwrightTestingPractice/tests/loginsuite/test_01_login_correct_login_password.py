import pytest
from playwright.async_api import Playwright
from playwrightTestingPractice.utils.utility import user_credentials,user_login
from playwrightTestingPractice.pages.login import Login
from playwrightTestingPractice.utils.login_register_utility import LoginRegister
from playwrightTestingPractice.pages.homepage import Homepage
@pytest.mark.parametrize('user_login',user_credentials)
def test_login(user_login,browserInstance1,click_login_register_button):
    logobject=Login(page=browserInstance1)
    logreg=LoginRegister(page=browserInstance1)
    user_email=user_login["Login name"]
    user_password=user_login["Password"]



    assert logobject.correct_login_details_check(user_email,user_password)=="I am a returning customer."
    