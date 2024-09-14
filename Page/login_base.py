from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from Page.base_page import BasePage
from common.driver_manager import chromeManager
from common.logger import logger
from data.config import Config as C


class LoginPage(BasePage):
    username_input = (By.XPATH, C.username_input)
    password_input = (By.XPATH, C.password_input)
    login_button = (By.XPATH, C.login_button)
    register_button = (By.XPATH, C.register_button)

    def __init__(self, driver: WebDriver = None):
        super().__init__(driver)
        driver.get(C.login_url)

    def login(self, username: str, password: str):
        """
        执行登录操作。
        @param username: 用户名。
        @param password: 密码。
        """
        logger.info("登录界面，执行登录操作")
        self.ele_send_key(self.username_input, username)
        self.ele_send_key(self.password_input, password)
        self.ele_click(self.login_button)


loginPage = LoginPage(chromeManager.driver)
if __name__ == '__main__':
    driver = loginPage.driver
    logger.info(driver)
    sleep(10)  # 可以调整等待时间

    # 确保退出时关闭 WebDriver
    driver.quit()
