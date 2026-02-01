import pytest
from playwrightTestingPractice.utils.utility import user_credentials,user_login
from playwrightTestingPractice.pages.login import Login
from playwrightTestingPractice.utils.login_register_utility import LoginRegister
from playwrightTestingPractice.pages.homepage import Homepage
from playwrightTestingPractice.testdata.testdata_file import incorrect_login_details

def test_incorrect_login_details(browserInstance,click_login_register_button):
    loginobj=Login(browserInstance)
    error_message=loginobj.enter_incorrect_login_details(incorrect_login_details)
    assert "Incorrect login or password provided" in error_message

    # logobject=Login(page=browserInstance)
    # logregobj=LoginRegister(page=browserInstance)
    # logregobj.navigation()
    # logregobj.click_login_register_button()

    #assert logobject.login(user_credentials) == "I am a returning customer."
    #assert logobject.login_verification()=="Welcome back QualityTester134"

