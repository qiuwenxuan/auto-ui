from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from config.conf import CHROME_PATH
from page.basePage import BasePage
from utils.parseConf import ParseConf


class LoginPage(BasePage):
    parseConf = ParseConf()
    # 登录网站url
    login_url = parseConf.get_value("Login", "login_url")
    # 用户名输入框
    username_input = parseConf.get_value("Login", "username_input")
    # 密码输入框
    password_input = parseConf.get_value("Login", "password_input")
    # 登录按钮
    login_button = parseConf.get_value("Login", "login_button")
    # 注册按钮
    register_button = parseConf.get_value("Login", "register_button")
    # 用户名错误定位器
    username_error_locator = parseConf.get_value("Login", "username_error_locator")
    # 密码错误定位器
    password_error_locator = parseConf.get_value("Login", "password_error_locator")
    # 记住用户复选框
    remember_user_checkbox = parseConf.get_value("Login", "remember_user_checkbox")
    # 忘记密码按钮
    forget_password_button = parseConf.get_value("Login", "forget_password_button")
    # 用户page获取账户信息定位器
    account_locator = parseConf.get_value("Login", "account_locator")

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def open_url(self):
        return self.load_url(self.login_url)

    def input_username(self, username):
        return self.send_keys(*self.username_input, username)

    def input_password(self, password):
        return self.send_keys(*self.password_input, password)

    def click_remember_user_checkbox(self):
        return self.select_checkbox(*self.remember_user_checkbox)

    def click_forget_password_button(self):
        return self.click(*self.forget_password_button)

    def click_login_button(self):
        return self.click(*self.login_button)

    def click_register_button(self):
        return self.click(*self.click_register_button)

    def get_username_err_text(self):
        return self.get_element_text(*self.username_error_locator)

    def get_password_err_text(self):
        return self.get_element_text(*self.password_error_locator)

    def get_account_text(self):
        return self.get_element_text(*self.account_locator)

    def get_login_err_text(self):
        return self.get_username_err_text() or self.get_password_err_text()

    def login(self, username, password):
        self.open_url()
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()


if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(CHROME_PATH))
    login_page = LoginPage(driver)
    login_page.login("qwx13057573527", "qwx#125617")
