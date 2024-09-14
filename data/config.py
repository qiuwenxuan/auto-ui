from util.config_loader import confloader


class Config:
    """env"""
    username = confloader.get_value("env", "username")
    password = confloader.get_value("env", "password")
    login_url = confloader.get_value("env", "login_url")

    """sql"""
    sql_file = confloader.get_value("sql", "sql_file")
    sql_delete = confloader.get_value("sql", "sql_delete")
    sql_insert = confloader.get_value("sql", "sql_insert")
    sql_select = confloader.get_value("sql", "sql_select")

    """login_page"""
    username_input = confloader.get_value("login_page", "username_input")
    password_input = confloader.get_value("login_page", "password_input")
    login_button = confloader.get_value("login_page", "login_button")
    register_button = confloader.get_value("login_page", "register_button")


if __name__ == '__main__':
    """env"""
    print("用户名: " + Config.username)
    print("密码: " + Config.password)
    print("登录URL: " + Config.login_url)

    """sql"""
    print("SQL文件路径: " + Config.sql_file)
    print("SQL删除语句: " + str(Config.sql_delete))
    print("SQL插入语句: " + str(Config.sql_insert))
    print("SQL查询语句: " + str(Config.sql_select))

    """login_page"""
    print("用户名输入框定位: " + Config.username_input)
    print("密码输入框定位: " + Config.password_input)
    print("登录按钮定位: " + Config.login_button)
    print("注册按钮定位: " + Config.register_button)
