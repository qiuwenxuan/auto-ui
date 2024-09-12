import sqlite3

from conftest import logger
from settings import DBSql


class MysqlAuto(object):
    def __init__(self):
        """连接到sql数据库"""
        self.conn = sqlite3.connect(DBSql.sql_file)
        # 创建一个游标
        self.cursor = self.conn.cursor()
        logger.info(f"链接数据库文件:{DBSql.sql_file}")

    def __del__(self):
        """对象资源被释放时触发，在对象即将被删除时的最后操作"""
        self.cursor.close()
        self.conn.close()

    def execute(self, sql_list):
        """执行sql语句"""
        try:
            for i in sql_list:
                logger.info(f"执行sql命令:{i}")
                self.cursor.execute(i)
                logger.debug(f"执行结果为:{self.cursor.fetchall()}")
            # 提交事务
            self.conn.commit()
            return self.cursor.fetchall()
        except Exception as e:
            logger.error(f"执行sql出现错误，异常为：{e}")
            raise e


if __name__ == '__main__':
    mysql = MysqlAuto()
    find_userinfo = ["select * from df_user_userinfo"]
    mysql.execute(DBSql.sql_list)
    mysql.execute(find_userinfo)
