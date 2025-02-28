from selenium.webdriver.common.by import By
from base_page import BasePage
from element_objects.header import HeaderElement


class CatalogPage(BasePage):
    PRODUCT = (By.CSS_SELECTOR, ".product-thumb")
    PRODUCT_COMPARE = (By.ID, "compare-total")
    SORT_BY = (By.ID, "input-sort")
    SHOW = (By.ID, "input-limit")
    SHOWING = (By.CSS_SELECTOR, ".col-sm-6.text-start")
    PAGES = (By.CSS_SELECTOR, ".col-sm-6.text-end")

    PRICE = (By.CSS_SELECTOR, ".price-new")
    CURRENCY = (By.CSS_SELECTOR, "form>.dropdown>a>.d-none.d-md-inline")
    EURO = (By.CSS_SELECTOR, "a[href='EUR']")

    def catalog_desktops_elements(self):
        checking_elements = [
            self.PRODUCT_COMPARE,
            self.PRODUCT,
            self.SHOWING,
            self.PAGES,
            self.SORT_BY,
            self.SHOW,
        ]
        self.wait_title("Desktops")
        return self.is_elements_list_present(checking_elements)

    def catalog_desktop_change_currency(self):
        self.wait_title("Desktops")

        price_first = self.get_text(self.PRICE)

        self.click_to_element(self.CURRENCY)
        self.click_to_element(self.EURO)

        price_second = self.get_text(self.PRICE)
        assert price_first != price_second, (
            f"price should be changed, initial price {price_first}, price after changing {price_second}"
        )

    def catalog_get_price(self):
        self.wait_title("Desktops")
        return self.get_text(self.PRICE)

    def catalog_change_currency(self):
        header = HeaderElement(self.browser, self.url)
        header.header_change_currency_gbp()
