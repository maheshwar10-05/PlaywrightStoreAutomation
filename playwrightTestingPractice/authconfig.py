import asyncio, os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://automationteststore.com/")

        # Click login
        await page.click("text=Login or register")

        # Fill credentials
        await page.fill("#loginFrm_loginname", "testuser36567")
        await page.fill("#loginFrm_password", "Testuser@1234")
        await page.click("button[title='Login']")

        await page.wait_for_load_state("networkidle")

        # SAVE LOGIN SESSION

        file_path = os.path.join(os.path.dirname(__file__), "auth.json")
        await context.storage_state(path=file_path)

        await browser.close()
if __name__ == "__main__":
    asyncio.run(main())

