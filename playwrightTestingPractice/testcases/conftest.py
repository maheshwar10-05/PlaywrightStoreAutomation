# conftest.py

import pytest
from playwright.async_api import Playwright
import time
from pytest_html import extras
import os
from playwrightTestingPractice.pageobjects.login import Login
from playwrightTestingPractice.Utilities.utility import user_credentials2,user_login2
from playwrightTestingPractice.Utilities.login_register_utility import LoginRegister
from playwrightTestingPractice.pageobjects.homepage import Homepage

SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit","edge"]


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="append",
        default=["chromium"],  # Ensure default is a list if using action="append"
        choices=SUPPORTED_BROWSERS,
        help="Specify the browser(s) to run tests on: chromium, firefox, webkit"
    )


def pytest_generate_tests(metafunc):
    # Check if the fixture 'browserInstance' is requested by a test
    if "browserInstance" in metafunc.fixturenames:
        # Get the list of browsers passed via the command line
        browsers = metafunc.config.getoption("browser_name")

        # KEY FIX: Parameterize the 'browserInstance' fixture 
        # using indirect=True so that request.param works inside the fixture.
        metafunc.parametrize("browserInstance", browsers, indirect=True, scope="function")


# Note: The user_parameters fixture is not needed for this setup and can be removed
# @pytest.fixture
# def user_parameters(request):
#     return request.param

@pytest.fixture
def browserInstance(playwright: Playwright, request):
    # This will now correctly receive the browser name from the parametrization
    browser_name = request.param

    # ... (Rest of your fixture logic)
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)  # <--- ADDED webkit logic
    # Optional: If you support 'chrome' and 'edge' as separate names in SUPPORTED_BROWSERS
    # elif browser_name == "chrome":
    #     browser = playwright.chromium.launch(headless=False, channel="chrome")
    elif browser_name == "edge":
        browser = playwright.chromium.launch(headless=False, channel="msedge")
    else:
        # Should not happen if 'choices' is used correctly
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context(
        capture_screenshot="Screenshots/" if "retain-on-failure" in request.config.getoption("--screenshot") else None
    )
    page = context.new_page()

    yield page
    
    # Cleanup
    browser.close()

@pytest.fixture

def common_steps(browserInstance):
    logregobj=LoginRegister(page=browserInstance)
    
    logregobj.navigation()
    logregobj.click_login_register_button()
    

#@pytest.fixture(params=user_credentials)
@pytest.fixture
def login_fixture(request,browserInstance):
    #user_data=request.param
    logobject=Login(page=browserInstance)
    homepage_categories=Homepage(page=browserInstance)
    logobject.login(user_credentials2)
    count1=logobject.click_home()
    return homepage_categories,count1




 

 

        


# Make sure your test uses the fixture:
# def test_login(browserInstance):
#     browserInstance.goto("https://...")