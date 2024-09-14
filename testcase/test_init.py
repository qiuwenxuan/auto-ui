from common.sql_manager import SQLManager
from data.config import Config


def test_sample(login):
    # 假设数据库数据已经初始化，可以直接进行断言
    result = SQLManager().execute(Config.sql_select)
    print(result)
    # assert True
