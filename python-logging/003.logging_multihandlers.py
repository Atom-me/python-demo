import logging
import sys

"""
控制台打印INIFO级别以上日志
文件打印DEBUG级别以上日志
"""

if __name__ == '__main__':
    FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'

    # 文件句柄，打印到文件
    file_handler = logging.FileHandler("multi_handlers.log")

    # 流句柄，打印到控制台
    stream_handler = logging.StreamHandler(sys.stdout)
    # 设置 INFO级别以及以上级别打印到控制台， 会覆盖 basicConfig 中设置的level参数
    stream_handler.setLevel(logging.INFO)

    logging.basicConfig(
        format=FORMAT,
        datefmt=DATE_FORMAT,
        level=logging.DEBUG,
        handlers=[file_handler, stream_handler])

    logging.debug('this is debug message ...')
    logging.info(' this info message ...')
    logging.warning('this is warning message ...')
    logging.error('this is error message ...')
    logging.critical('this is critical message ...')
