import pytest
from playwrightTestingPractice.utils.utility import user_credentials,user_login
from playwrightTestingPractice.pages.login import Login
from playwrightTestingPractice.utils.login_register_utility import LoginRegister
from playwrightTestingPractice.pages.homepage import Homepage
from playwrightTestingPractice.testdata.testdata_file import login_correct_incorrect_password

def test_correct_login_incorrect_password(browserInstance,click_login_register_button):
    loginobj=Login(browserInstance)
    error_message=loginobj.enter_correct_login_name_incorrect_password(login_correct_incorrect_password)
    assert "Incorrect login or password provided" in error_message

    # logobject=Login(page=browserInstance)
    # logregobj=LoginRegister(page=browserInstance)
    # logregobj.navigation()
    # logregobj.click_login_register_button()

    #assert logobject.login(user_credentials) == "I am a returning customer."
    #assert logobject.login_verification()=="Welcome back QualityTester134"

