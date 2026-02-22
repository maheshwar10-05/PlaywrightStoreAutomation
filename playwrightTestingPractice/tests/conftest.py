# conftest.py
from pathlib import Path
import pytest
import allure
import os
from playwright.sync_api import Playwright
from playwrightTestingPractice.pages.login import Login
from playwrightTestingPractice.pages.homepage import Homepage
from playwrightTestingPractice.utils.utility import user_credentials2

# -------------------------
# CONFIG PATHS
# -------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_DIR = os.path.join(BASE_DIR, "reports")
TRACE_DIR = os.path.join(REPORT_DIR, "traces")
SCREENSHOT_DIR = os.path.join(REPORT_DIR, "screenshots")

os.makedirs(TRACE_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit", "edge"]

# -------------------------
# PYTEST CLI OPTION
# -------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="append",
        default=["chromium"],
        # choices=SUPPORTED_BROWSERS,
        help="Browsers: chromium, firefox, webkit, edge"
    )

# -------------------------
# PARAMETERIZE BROWSERS
# -------------------------
# def pytest_generate_tests(metafunc):
    # if "browser_name" in metafunc.fixturenames:
        # browsers = metafunc.config.getoption("browser_name")
        # metafunc.parametrize("browser_name", browsers, scope="session")

# -------------------------
# BROWSER FIXTURE (SESSION)
# -------------------------
@pytest.fixture(scope='session')
def browser(playwright: Playwright, browser_name):
    
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=True)
    elif browser_name == "edge":
        browser = playwright.chromium.launch(headless=True, channel="msedge")
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield browser
    browser.close()

# -------------------------
# PAGE FIXTURE (fail tests)
@pytest.fixture
def browserInstance(browser, request):

    AUTH_FILE = Path(__file__).resolve().parent.parent / "auth.json"
    context = browser.new_context(storage_state=str(AUTH_FILE))
    page = context.new_page()
    page.goto("https://automationteststore.com/")

    # Start trace for every test (cheap)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Store for other fixtures/hooks
    request.node.context = context
    request.node.page = page

    yield page

    # ===============================
    # SAVE TRACE ONLY IF FAILED
    # ===============================
    if request.node.rep_call.failed:
        test_name = request.node.nodeid.replace("::", "_").replace("/", "_")
        trace_path = os.path.join(TRACE_DIR, f"{test_name}.zip")
        context.tracing.stop(path=trace_path)
        print(f"❌ Trace saved: {trace_path}")
    else:
        # Discard trace if passed
        context.tracing.stop()
        print("✅ Trace discarded (test passed)")

    # Close context
    context.close()
@pytest.fixture
def browserInstance1(browser,request):
        context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
        page = context.new_page()
        page.goto("https://automationteststore.com/")
        yield page
        context.close()
# -------------------------
# LOGIN FIXTURE
# -------------------------
@pytest.fixture
def click_login_register_button(browserInstance1):
    browserInstance1.get_by_role("link", name="Login or register").click()
    
@pytest.fixture
def login_fixture(browserInstance1):
    logobject = Login(page=browserInstance1)
    homepage_categories = Homepage(page=browserInstance1)
    logobject.login(user_credentials2)
    count1 = logobject.click_home()
    return homepage_categories, count1
# -------------------------
# STORE TEST RESULT
# -------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep

# -------------------------
# ATTACH TRACE + SCREENSHOT ONLY FAILED
# -------------------------
@pytest.fixture(autouse=True)
def attach_on_failure(request):
    yield
    TRACE_DIR1 = Path("reports/traces")
    # If pytest hook didn't run, exit safely
    if not hasattr(request.node, "rep_call"):
        return

    if request.node.rep_call.failed:
        test_name = request.node.nodeid.replace("::", "_").replace("/", "_")
        trace_file = TRACE_DIR1 / f"{test_name}.zip"

        if trace_file.exists():
            allure.attach.file(
                str(trace_file),
                name="Playwright Trace",
                attachment_type=allure.attachment_type.ZIP
            )
@pytest.fixture
def home_fixture(browserInstance):
    homepage_categories = Homepage(page=browserInstance)
    return homepage_categories
    
