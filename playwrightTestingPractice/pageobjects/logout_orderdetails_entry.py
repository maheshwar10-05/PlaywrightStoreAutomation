class EnterOrder:
    def __init__(self,page):
        self.page=page

    def order_input(self):
        self.page.locator("#CheckOrderFrm_order_id").fill("68568")
        self.page.locator("#CheckOrderFrm_email").fill("quality23@gmail.com")
        self.page.get_by_role("button", name="Continue").click()