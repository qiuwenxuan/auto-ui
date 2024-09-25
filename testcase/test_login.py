import pytest
from data.login_data import LoginData


class TestLogin(object):
    """登录用例"""

    login_data = LoginData()

    @pytest.mark.parametrize(
        "username, password, expect",
        login_data.login_success_data,
        ids=login_data.login_success_ids,
    )
    def test_login_success(self, ini_page, username, password, expect):
        login_page = ini_page
        login_page.login(username, password)
        account = login_page.get_account_text()
        assert account == expect

    @pytest.mark.parametrize(
        "username, password, expect",
        login_data.login_fail_data,
        ids=login_data.login_fail_ids,
    )
    def test_login_fail(self, ini_page, username, password, expect):
        login_page = ini_page
        login_page.login(username, password)
        text = login_page.get_login_err_text()
        assert text == expect
