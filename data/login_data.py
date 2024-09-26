class LoginData(object):
    """用户登录测试数据"""

    login_success_data = [("qwx13057573527", "qwx#125617", "qwx13057573527")]
    login_success_ids = ["test_login_001"]

    login_fail_data = [
        ("13057573527", "qwx#125617", "用户名错误"),
        ("qwx13057573527", "125617", "密码错误"),
        ("", "qwx#125617", "用户名"),
        ("qwx13057573527", "", "密码"),
    ]
    login_fail_ids = [
        "test_login_002",
        "test_login_003",
        "test_login_004",
        "test_login_005",
    ]
