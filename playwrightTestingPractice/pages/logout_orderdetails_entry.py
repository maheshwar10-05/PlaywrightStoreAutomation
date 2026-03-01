class EnterOrder:
    def __init__(self, page):
        self.page = page
        
        # --- LOCATORS ---
        self.order_id_input = self.page.locator("#CheckOrderFrm_order_id")
        self.email_input = self.page.locator("#CheckOrderFrm_email")
        self.continue_btn = self.page.get_by_role("button", name="Continue")

    async def order_input(self, order_id: str = "68568", email: str = "quality23@gmail.com"):
        """
        Inputs order details and clicks continue. 
        Parametrized with defaults to keep your original values.
        """
        # Await the filling of fields
        await self.order_id_input.fill(order_id)
        await self.email_input.fill(email)
        
        # Await the click action
        await self.continue_btn.click()
        
        # Optional: You might want to await a navigation or header check here
        # await self.page.wait_for_load_state("networkidle")