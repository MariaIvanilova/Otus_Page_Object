from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(url=self.url)

    def is_element_present(self, locator: tuple):
        try:
            return self.browser.find_element(*locator)
        except NoSuchElementException:
            return False

    def is_elements_list_present(self, elements: list):
        for locator in elements:
            try:
                self.browser.find_element(*locator)
            except NoSuchElementException:
                self.browser.save_screenshot(f"{self.browser.session_id}.png")
                raise AssertionError(f"Element with locator:{locator} is absent")
        return True

    def wait_title(self, title, timeout=3):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.title_is(title))
        except TimeoutException:
            raise AssertionError(
                f"Expected title is {title}, but title is {self.browser.title}"
            )

    def wait_element(self, locator, timeout=1):
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            self.browser.save_screenshot(f"{self.browser.session_id}.png")
            raise AssertionError(f"Didn't wait for: {locator}")

    def wait_text(self, locator, text, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            raise AssertionError(f"Didn't wait for text: {text} in locator: {locator}")

    def input_value_to_field(self, locator: tuple, key_value: str):
        self.browser.find_element(*locator).send_keys(key_value)

    def click_to_element(self, locator: tuple):
        self.browser.find_element(*locator).click()

    def action_chains_click(self, locator: tuple):
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(locator)
        )
        ActionChains(self.browser).move_to_element(element).pause(1).click().pause(
            1
        ).perform()

    def get_text(self, locator: tuple):
        return self.browser.find_element(*locator).text

    def scroll_to_element(self, locator: tuple):
        self.browser.execute_script(
            "arguments[0].scrollIntoView(true);", self.browser.find_element(*locator)
        )

    def scroll_to_up(self):
        self.browser.execute_script("window.scrollTo(0, 0)")

    def alert_confirm(self):
        self.browser.switch_to.alert.accept()
