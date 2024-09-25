import sqlite3

from common.logger import LoggerManager
from config.conf import SQL_FILE
from utils.parseConf import ParseConf
from conftest import logger

class SQLManager(object):
    parseConf = ParseConf()
    sql_delete = [sql.strip() for sql in parseConf.get_value('SQL', 'sql_delete').split(",")]
    sql_insert = [parseConf.get_value('SQL', 'sql_insert')]
    sql_select = [parseConf.get_value('SQL', 'sql_select')]

    def __init__(self, default_file=SQL_FILE):
        """连接到sql数据库"""
        self.conn = sqlite3.connect(default_file)
        # 创建一个游标
        self.cursor = self.conn.cursor()
        logger.info(f"连接数据库资源，数据库文件:{default_file}")

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
                logger.debug(f"执行结果为:{result}")
            # 提交事务
            self.conn.commit()
            return result
        except Exception as e:
            logger.error(f"执行sql出现错误，异常为：{e}")
            raise e

    def setup_sql(self):
        logger.info("正在初始化测试数据...")
        self.execute(self.sql_delete)
        self.execute(self.sql_insert)
        logger.info(f"初始化测试数据完成，初始化数据为:{self.execute(self.sql_select)}")


if __name__ == '__main__':
    sm = SQLManager()
    sm.setup_sql()
