import pytest
from playwrightTestingPractice.utils.utility import user_credentials,user_login
from playwrightTestingPractice.pages.login import Login
from playwrightTestingPractice.utils.login_register_utility import LoginRegister
from playwrightTestingPractice.pages.homepage import Homepage

@pytest.mark.parametrize('user_login',user_credentials)
def test_login(user_login,browserInstance):
    logobject=Login(page=browserInstance)
    user_email=user_login["Login name"]
    user_password=user_login["Password"]
    logregobj=LoginRegister(page=browserInstance)
    logregobj.navigation()
    logregobj.click_login_register_button()

    assert logobject.login(user_email,user_password)=="I am a returning customer."
    

    # logobject=Login(page=browserInstance)
    # logregobj=LoginRegister(page=browserInstance)
    # logregobj.navigation()
    # logregobj.click_login_register_button()

    #assert logobject.login(user_credentials) == "I am a returning customer."
    #assert logobject.login_verification()=="Welcome back QualityTester134"

