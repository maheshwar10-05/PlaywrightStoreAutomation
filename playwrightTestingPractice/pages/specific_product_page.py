import asyncio
from playwright.async_api import Page
from pathlib import Path

class Specificproduct:

    def __init__(self, page: Page):
        self.page = page
        
        # --- LOCATORS ---
        self.product_heading = self.page.locator(".bgnone")
        self.quantity_input = self.page.locator("#product_quantity")
        self.price_container = self.page.locator("//div[@class='productfilneprice']")
        self.add_to_cart_btn = self.page.get_by_role("link", name="Add to Cart")
        self.price_label = self.page.locator("//label[@class='control-label']").first
        self.total_price_value = self.page.locator('span.total-price')
        self.print_btn = self.page.get_by_role("link", name="Print")

    async def product_specific(self,test_name="product_page"):
        base_dir = Path(__file__).resolve().parent.parent # Adjust '.parent' count based on folder depth
        output_dir = base_dir / "reports" / "pdf_outputs"
        price_dict = {}
        
        # Await text content
        heading3 = await self.product_heading.text_content()
        print(heading3)
        
        # Actions must be awaited
        await self.quantity_input.clear()
        await self.quantity_input.fill("4")
        await self.price_container.click()
        await self.add_to_cart_btn.click()
        
        # Navigation
        await self.page.go_back()
        
        # Replace time.sleep with async wait
        await self.page.wait_for_timeout(4000)
        
        # Fetching dynamic text
        raw_price_key = await self.price_label.text_content()
        price_key = raw_price_key.strip().removesuffix(":\xa0\xa0\n\t\t\t\t\t\t\t\t\t\t\t$150.00")
        
        price_value = await self.total_price_value.text_content()
        price_dict[price_key] = price_value
        
        await self.print_btn.click()
        pdf_path = output_dir / f"{test_name}.pdf"
        # Note: .pdf() only works in Headless mode
        try:
            # 4. Generate the PDF
            await self.page.pdf(path=str(pdf_path), format="A4")
            print(f"✅ PDF saved successfully: {pdf_path}")
        except Exception as e:
            print(f"PDF generation failed (likely not in headless mode): {e}")
            
        await self.page.wait_for_timeout(8000)
        print(price_dict)
        return price_dict

    async def add_review_specific(self):
        # Await methods for the review logic
        heading3 = await self.product_heading.text_content()
        print(heading3)
        await self.quantity_input.clear()
        await self.quantity_input.fill("4")
        await self.price_container.click()
        await self.add_to_cart_btn.click()