import pytest
from data.login_data import LoginData


class TestLogin(object):
    """登录用例"""

    login_data = LoginData()

    @pytest.mark.parametrize(
        "username, password, expect", login_data.login_success_data
    )
    def test_login_success(self, ini_page, username, password, expect):
        login_page = ini_page
        login_page.login(username, password)
        account = login_page.get_account_text()
        assert expect in account

    @pytest.mark.parametrize(
        "username, password, expect", login_data.login_fail_data
    )
    def test_login_fail(self, ini_page, username, password, expect):
        login_page = ini_page
        login_page.login(username, password)
        login_page.
        assert expect in account
