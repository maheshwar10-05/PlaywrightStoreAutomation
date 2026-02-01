import pytest,openpyxl
from playwrightTestingPractice.utils.utility import user_credentials,user_login
from playwrightTestingPractice.pages.login import Login
from playwrightTestingPractice.utils.login_register_utility import LoginRegister
from playwrightTestingPractice.pages.homepage import Homepage
from playwrightTestingPractice.testdata.testdata_file import Data

list1=Data().data_login_details()

@pytest.mark.parametrize('user_list1',list1)
def test_excel_data(user_list1,browserInstance,click_login_register_button):
    loginobj=Login(browserInstance)
    user_name=user_list1["user"]
    user_password=user_list1["pass"]

    login_name, error_message = loginobj.excel_data_login_password(
    user_name, user_password
)

    if login_name:
        assert "Welcome" in login_name
        assert error_message is None
    else:
        assert error_message is not None

