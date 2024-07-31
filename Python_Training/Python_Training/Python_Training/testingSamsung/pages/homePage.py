from selenium.webdriver.common.by import By


class homePage():
    def __init__(self,driver):
        self.driver = driver
        self.phone = "Galaxy S24 Ultra"
        self.search_Icon = "nv00-gnb__utility-btn.gnb__search-btn-js"
        self.search_submit = "gnb-search__input-btn--search"
        self.search_Bar = "gnb-search__input"

    def search_Function(self):
        search_Icon = self.driver.find_element(By.CLASS_NAME, self.search_Icon)
        search_submit = self.driver.find_element(By.CLASS_NAME, self.search_submit)
        search_Icon.click()
        search_Bar = self.driver.find_element(By.CLASS_NAME, self.search_Bar)
        search_Bar.send_keys(self.phone)
        search_submit.click()