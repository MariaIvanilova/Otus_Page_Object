from selenium.webdriver.common.by import By
from base_page import BasePage


class HeaderElement(BasePage):
    CURRENCY = (By.CSS_SELECTOR, "form>.dropdown>a>.d-none.d-md-inline")
    EURO = (By.CSS_SELECTOR, "a[href='EUR']")
    POUND = (By.CSS_SELECTOR, "a[href='GBP']")
    USD = (By.CSS_SELECTOR, "a[href='USD']")
    CURRENCY_SIGN = (By.CSS_SELECTOR, ".dropdown>a>strong")

    def header_change_currency_eur(self):
        self.click_to_element(self.CURRENCY)
        self.click_to_element(self.EURO)
        return self.get_text(self.CURRENCY_SIGN)

    def header_change_currency_gbp(self):
        self.click_to_element(self.CURRENCY)
        self.click_to_element(self.POUND)
        return self.get_text(self.CURRENCY_SIGN)

    def header_change_currency_usd(self):
        self.click_to_element(self.CURRENCY)
        self.click_to_element(self.USD)
        return self.get_text(self.CURRENCY_SIGN)
