import pytest
from playwright.async_api import Playwright
from playwrightTestingPractice.utils.utility import user_credentials,user_login
from playwrightTestingPractice.pages.login import Login
from playwrightTestingPractice.utils.login_register_utility import LoginRegister
from playwrightTestingPractice.pages.homepage import Homepage
@pytest.mark.parametrize('user_login',user_credentials)
@pytest.mark.no_auth
async def test_login(user_login,browserInstance,click_login_register_button):
    logobject=Login(page=browserInstance)
    logreg=LoginRegister(page=browserInstance)
    user_email=user_login["Login name"]
    user_password=user_login["Password"]



    assert "Welcome back"  in await logobject.correct_login_details_check(user_email,user_password)
    