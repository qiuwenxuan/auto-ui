import sqlite3

from conftest import logger
from data.constant import SQL


class SQLManager(object):
    def __init__(self):
        """连接到sql数据库"""
        self.conn = sqlite3.connect(SQL.SQL_FILE)
        # 创建一个游标
        self.cursor = self.conn.cursor()
        logger.info(f"链接数据库文件:{SQL.SQL_FILE}")

    def __del__(self):
        """对象资源被释放时触发，在对象即将被删除时的最后操作"""
        self.cursor.close()
        self.conn.close()

    def execute(self, sql_list):
        """执行sql语句"""
        result = None
        try:
            for i in sql_list:
                logger.info(f"执行sql命令:{i}")
                self.cursor.execute(i)
                result = self.cursor.fetchall()
                logger.info(f"执行结果为:{result}")
            # 提交事务
            self.conn.commit()
            return result
        except Exception as e:
            logger.error(f"执行sql出现错误，异常为：{e}")
            raise e


sm = SQLiteManager()

if __name__ == '__main__':
    mysql = sqlObject
    # mysql.execute(DBSql.sql_list)

    mysql.execute(["SELECT * FROM df_user_userinfo"])
    mysql.execute(["SELECT uname FROM df_user_userinfo WHERE uname='wenxuan1'"])

    # mysql.execute(["DELETE FROM df_order_orderdetailinfo",
    #                "DELETE FROM df_order_orderinfo",
    #                "DELETE FROM df_user_userinfo",
    #                "DELETE FROM df_cart_cartinfo"])

    # mysql.execute([
    #     "INSERT INTO df_user_userinfo VALUES (40, 'b444ac06613fc8d63795be9ad0beaf55011936ac', '898787869@qq.com', 'test1', '广州市天河区棠下东街101号', '51200', '12345678989', 'test1'), (41, 'd0b70dd55b42b70af6069de0a8c0a51fd9d27171', 'qwx13057573527@163.com', '', '', '', '', 'qwx13057573527')"])
