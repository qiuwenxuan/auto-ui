from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from Page.base_page import BasePage
from common.driver_manager import DriverManager
from common.logger import logger


class LoginPage(BasePage):
    sel_username_input = (By.XPATH, '//*[@placeholder="请输入用户名"]')
    sel_password_input = (By.XPATH, '//*[@placeholder="请输入密码"]')
    sel_login_button = (By.XPATH, '//input[@value="登录"]')
    sel_register_button = (By.XPATH, '//a[@href|text()="立即注册"]')

    def __init__(self, driver: WebDriver = None):
        super().__init__(driver)
        driver.get(LOGIN_URL)

    def login(self, username, password):
        # 输入账户和密码
        logger.info(f"登录界面，执行登录操作")
        self.ele_send_key(self.driver, self.sel_username_input, username)
        self.ele_send_key(self.driver, self.sel_password_input, password)

        # 点击登录
        self.ele_click(self.driver, self.sel_login_button)


if __name__ == '__main__':
    driver = DriverManager.get_edgedriver()
    login_page = LoginPage(driver)
