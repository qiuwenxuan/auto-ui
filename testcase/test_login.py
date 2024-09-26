import pytest
import allure
from data.login_data import LoginData

from page.loginPage import LoginPage


# epic->feature->story->title->step
@allure.epic("自动化项目")  # 项目名
@allure.feature("登录模块")  # 模块名
@allure.story("登录")  # 子模块名
class TestLogin(object):
    """登录用例"""

    login_data = LoginData()

    @allure.title("用户正确登录用户名密码")  # 标题名
    @pytest.mark.parametrize(
        "username, password, expect",
        login_data.login_success_data,
        ids=login_data.login_success_ids,
    )
    def test_login_success(self, ini_page: LoginPage, username, password, expect):
        with allure.step("1.进入登录界面"):  # 步骤名
            login_page = ini_page
        with allure.step("2.登录用户名密码"):
            login_page.login(username, password)
        with allure.step("3.获取登录后账户信息"):
            account = login_page.get_account_text()
        with allure.step("4.断言登录账户是否正确"):
            assert account == expect

    @allure.title("用户错误登录用户名密码")
    @pytest.mark.parametrize(
        "username, password, expect",
        login_data.login_fail_data,
        ids=login_data.login_fail_ids,
    )
    def test_login_fail(self, ini_page: LoginPage, username, password, expect):
        with allure.step("1.进入登录界面"):
            login_page = ini_page
        with allure.step("2.登录用户名密码"):
            login_page.login(username, password)
        with allure.step("3.获取登录后账户信息"):
            if "用户名" in expect:
                text = login_page.get_username_err_text()
            elif "密码" in expect:
                text = login_page.get_password_err_text()
        with allure.step("4.断言登录账户是否正确"):
            assert text == expect
