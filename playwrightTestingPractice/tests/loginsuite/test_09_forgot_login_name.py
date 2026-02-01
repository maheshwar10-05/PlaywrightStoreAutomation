import pytest,openpyxl,logging
from playwrightTestingPractice.utils.utility import user_credentials,user_login
from playwrightTestingPractice.pages.login import Login
from playwrightTestingPractice.utils.login_register_utility import LoginRegister
from playwrightTestingPractice.pages.homepage import Homepage
from playwrightTestingPractice.testdata.testdata_file import Data

list1=Data().forgot_login_details()

@pytest.mark.parametrize('user_list1',list1)
def test_excel_data(user_list1,browserInstance,click_login_register_button):
    loginobj=Login(browserInstance)
    last_name=user_list1["last_name"]
    email=user_list1["email"]

    error_message,success_message = loginobj.forgot_login(last_name, email)
    logging.info(success_message)
    logging.info(error_message)

    if success_message:
        assert "Success" in success_message
        assert error_message is None
    else:
        assert error_message is not None
        


