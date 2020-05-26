from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver1=None):
        if driver1 == None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self.driver: WebDriver = driver1
        self.driver.implicitly_wait(3)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        return self.driver.find_elements(by, value)

    def waitfor_click(self, ele, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(ele))

    def quit(self):
        return self.driver.quit()
