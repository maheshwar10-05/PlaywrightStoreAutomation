import asyncio
from playwright.async_api import Page

class Subaccessory:
    def __init__(self, page: Page):
        self.page = page
        
        # --- LOCATORS ---
        # Base locator for products in the grid
        self.fragrance_products = self.page.locator("//div[@class='col-md-3 col-sm-6 col-xs-12']/div[1]/div/a")
        
    async def view_product(self):
        # 1. Await the count to get an integer
        count = await self.fragrance_products.count()
        #In Python lists and Playwright locators, indices are zero-based ($0, 1, 2, ...$).If you initialized index = 0, and your code failed to find the product, your script might accidentally try to click the first item on the page because it thinks it found a match at position 0.-1 is an impossible index for a list of elements, so it clearly indicates that the search failed.
        index = -1

        # 2. Loop through to find the specific product
        for i in range(count):
            # Check if this specific nth element has the required text
            if await self.fragrance_products.nth(i).filter(has_text="MAN Eau de Toilette Spray").count() > 0:
                index = i
                print(f"Product found at index: {index}")
                
                # Dynamic Logic for Hover and Click based on index
                # We use the index to build the specific locator for that grid item
                if index < 4:
                    item_pos = index + 1
                else:
                    item_pos = index + 2
                
                # Define dynamic locators for the specific thumbnail found
                thumbnail_img = self.page.locator(f"//div[@class='thumbnails grid row list-inline']//div[{item_pos}]//div[2]//a[1]//img[1]")
                view_button = self.page.locator(f"//div[@class='thumbnails grid row list-inline']//div[{item_pos}]//div[2]//div[1]//a[1]")
                
                # 3. Perform Awaited Actions
                await thumbnail_img.hover()
                await view_button.click()
                
                # Break once the product is found and clicked
                break
        
        if index == -1:
            print("Product 'MAN Eau de Toilette Spray' not found in the list.")