import pytest

from page.loginPage import LoginPage


# 初始化所有页面的driver
@pytest.fixture(scope="module")
def ini_page(driver):
    login_page = LoginPage(driver)
    yield login_page
