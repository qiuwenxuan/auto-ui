from common.sql_manager import SQLManager
from data.config import SQL_SELECT


def test_sample():
    # 假设数据库数据已经初始化，可以直接进行断言
    result = SQLManager().execute(SQL_SELECT)
    print(result)
    # assert True
