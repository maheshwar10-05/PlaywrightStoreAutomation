# conftest.py
from pathlib import Path
import pytest
import allure
import os
from playwright.async_api import Playwright,async_playwright
import asyncio
from playwrightTestingPractice.pages.login import Login
from playwrightTestingPractice.pages.homepage import Homepage
from playwrightTestingPractice.utils.utility import user_credentials2

# -------------------------
# CONFIG PATHS
# -------------------------
CONFTEST_DIR = Path(__file__).resolve().parent

# 2. Go UP one level to the project root (e.g., .../project)
# If your conftest.py is already at the root, remove the .parent
PROJECT_ROOT = CONFTEST_DIR.parent 

# 3. Define absolute paths based on the Project Root
REPORT_DIR = PROJECT_ROOT / "reports"
TRACE_DIR = REPORT_DIR / "traces"
ALLURE_RESULTS_DIR = REPORT_DIR / "allure-results"

# 4. Ensure these folders exist at the root
TRACE_DIR.mkdir(parents=True, exist_ok=True)
ALLURE_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

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
def pytest_generate_tests(metafunc):
    if "browser_name_parameterize" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("browser_name")
        metafunc.parametrize("browser_name_parameterize", browsers, scope="session")

# -------------------------
# BROWSER FIXTURE (SESSION)
# -------------------------
@pytest.fixture(scope='session')
async def browser(browser_name_parameterize):

    async with async_playwright() as playwright:
        if browser_name_parameterize == "chromium":
            browser = await playwright.chromium.launch(headless=True)
        elif browser_name_parameterize == "firefox":
            browser = await playwright.firefox.launch(headless=True)
        elif browser_name_parameterize == "webkit":
            browser = await playwright.webkit.launch(headless=True)
        elif browser_name_parameterize == "edge":
            browser = await playwright.chromium.launch(headless=True, channel="msedge")
        else:
            raise ValueError(f"Unsupported browser: {browser_name_parameterize}")

        yield browser
        await browser.close()

# -------------------------
# PAGE FIXTURE (fail tests)
@pytest.fixture
async def browserInstance(browser, request):
    # Check if the test has the @pytest.mark.no_auth marker
    no_auth_marker = request.node.get_closest_marker("no_auth")
    AUTH_FILE = Path(__file__).resolve().parent.parent / "auth.json"
    
    # Logic: Load auth only if marker is NOT present AND file exists
    if no_auth_marker or not AUTH_FILE.exists():
        print("\n Running as GUEST (no auth)")
        context = await browser.new_context()
    else:
        print("\n Running as AUTHENTICATED user")
        context = await browser.new_context(storage_state=str(AUTH_FILE))

    await context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = await context.new_page()
    await page.goto("https://automationteststore.com/")

    
    # Store for other fixtures/hooks
    request.node.context = context
    request.node.page = page

    yield page

# --- Teardown Logic ---
    report = getattr(request.node, "rep_call", None)
    
    if report and report.failed:
        # Clean the test name for the filename
        test_name = request.node.nodeid.replace("::", "_").replace("/", "_").replace(".py", "")
        trace_path = TRACE_DIR / f"{test_name}.zip"
        
        # STOP and SAVE the trace
        await context.tracing.stop(path=str(trace_path))
        
        # Attach to Allure immediately while we have the file path
        allure.attach.file(
            str(trace_path),
            name=f"Trace_{test_name}",
            attachment_type="application/zip",
            extension="zip"
        )
    else:
        await context.tracing.stop()

    # Close context
    await context.close()

# -------------------------
# LOGIN FIXTURE
# -------------------------
@pytest.fixture
async def click_login_register_button(browserInstance):
    reg_log=browserInstance.get_by_role("link", name="Login or register")
    await reg_log.click()
    
@pytest.fixture
async def login_fixture(browserInstance):
    logobject = Login(page=browserInstance)
    await logobject.login(user_credentials2)
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
# @pytest.fixture(autouse=True)
# async def attach_on_failure(request):
#     yield
#     TRACE_DIR1 = Path("reports/traces")
#     # If pytest hook didn't run, exit safely
#     if not hasattr(request.node, "rep_call"):
#         return

#     if request.node.rep_call.failed:
#         test_name = request.node.nodeid.replace("::", "_").replace("/", "_")
#         trace_file = TRACE_DIR1 / f"{test_name}.zip"

#         if trace_file.exists():
#             allure.attach.file(
#                 str(trace_file),
#                 name="Playwright Trace",
#                 attachment_type=allure.attachment_type.ZIP
#             )
@pytest.fixture
async def home_fixture(browserInstance):
    homepage_categories = Homepage(page=browserInstance)
    return homepage_categories
    
