class ENV:
    """环境变量"""
    url = "http://127.0.0.1:8000/user/login/"


class DBSql:
    sql_file = r"C:\Users\v-williamqiu\Desktop\wx\workspace\DailyFresh\daily_fresh_demo-master\db.sqlite3"
    sql_list = [
        "DELETE FROM df_order_orderdetailinfo",
        "DELETE FROM df_order_orderinfo",
        "DELETE FROM df_user_userinfo",
        "DELETE FROM df_cart_cartinfo",
        "INSERT INTO 'df_user_userinfo' VALUES(41, 'd0b70dd55b42b70af6069de0a8c0a51fd9d27171', 'qwx13057573527@163.com', '', '', '', '', 'qwx13057573527'),"
        "(40, 'b444ac06613fc8d63795be9ad0beaf55011936ac', '898787869@qq.com', 'test1', '广州市天河区棠下东街101号', '51200', '12345678989', 'test1')",
        "SELECT * FROM df_user_userinfo"
    ]
