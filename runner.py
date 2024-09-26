import pytest
import os

from config.conf import CASE_DIR, RESULT_DIR, REPORT_DIR


if __name__ == "__main__":
    try:
        # 1. 清理json数据文件并使用pytest生成测试报告
        args_list = []  # 相当于python -m pytest,额外参数在pytest.ini文件内设置
        pytest.main(args_list)

        # 2. 使用allure命令生成测试报告 ：allure generate 数据路径文件 -o html路径文件 -c
        generate_cmd = rf"allure generate {RESULT_DIR} -o {REPORT_DIR} --clean"
        print(generate_cmd)
        os.system(generate_cmd)

        # 3. 自动弹出生成测试报告命令
        open_cmd = f"allure open {REPORT_DIR}"
        os.system(open_cmd)
    except KeyboardInterrupt:  # 出现KeyboardInterrupt异常不处理
        pass
