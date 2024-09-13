from util.config_loader import confloader

USERNAME = confloader.get_value("env", "username")
PASSWORD = confloader.get_value("env", "password")
URL = confloader.get_value("env", "url")

SQL_FILE = confloader.get_value("sql", "sql_file")
SQL_LIST = confloader.get_value("sql", "sql_list")

if __name__ == '__main__':
    print("用户名:" + USERNAME)
    print(SQL_LIST)
