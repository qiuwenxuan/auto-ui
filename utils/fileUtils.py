import os
from config.conf import IMAGE_DIR, LOG_DIR, LOG_PATH, REPORT_DIR, RESULT_DIR
from common.logger import logger


class FileUtils(object):
    """文件工具类"""

    @staticmethod
    def clean_folder(folder_path):
        """清空指定目录下的所有文件和文件夹"""
        if not os.path.exists(folder_path):
            logger.debug(f"目录 {folder_path} 不存在")
            return

        # root, dirs, files分别代表当前路径、该路径下的子目录和文件
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)  # 删除文件
                    logger.debug(f"已删除文件: {file_path}")
                except Exception as e:
                    logger.error(f"删除 {file_path} 失败。原因: {e}")

    @staticmethod
    def clean_image_data():
        """删除image下所有图片"""
        FileUtils.clean_folder(IMAGE_DIR)

    @staticmethod
    def clean_allure_result():
        """删除allure生成的result文件夹下所有数据文件"""
        FileUtils.clean_folder(RESULT_DIR)

    @staticmethod
    def clean_TestReport():
        """删除测试报告文件"""
        FileUtils.clean_folder(REPORT_DIR)

    @staticmethod
    def clean_log_data():
        """清空日志文件内容"""
        if os.path.exists(LOG_PATH):
            try:
                with open(LOG_PATH, "w") as f:
                    # 打开文件后直接关闭，内容被清空
                    pass
            except Exception as e:
                logger.debug(f"清空日志文件失败，异常: {e}")
        else:
            logger.error(f"日志文件 {LOG_PATH} 不存在")

    @staticmethod
    def clean_testcase_data():
        """删除所有测试数据"""
        try:
            FileUtils.clean_image_data()
            FileUtils.clean_allure_result()
            FileUtils.clean_TestReport()
            FileUtils.clean_log_data()
            logger.debug("测试数据删除成功")
        except Exception as e:
            logger.error(f"测试数据删除失败，异常为：{e}")


if __name__ == "__main__":
    FileUtils.clean_testcase_data()
