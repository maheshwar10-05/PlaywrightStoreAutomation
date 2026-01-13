import json
import time

from playwrightTestingPractice.pageobjects.registerpageobjects import Register
from playwrightTestingPractice.Utilities.utility import userdetails
from playwrightTestingPractice.Utilities.login_register_utility import LoginRegister



def test_create_account(browserInstance):
    reglogObj = LoginRegister(page=browserInstance)
    registerobject=Register(page=browserInstance)
    reglogObj.navigation()
    reglogObj.click_login_register_button()
    assert registerobject.account_login_page() == "Account Login"
    text1,text2 =registerobject.enter_details_to_create_account(userdetails)
    assert text1=="Create Account"
    
    assert text2=="Your Account Has Been Created!"
    