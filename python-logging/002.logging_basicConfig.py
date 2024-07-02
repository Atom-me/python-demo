import logging

"""
asctime: 日志生成时间
levelname: 日志等级
message: 日志内容
"""
logging.basicConfig(level=logging.DEBUG, filename='demolog.log', filemode='a',
                    format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.info(' this info message ...')
logging.debug('this is debug message ...')
logging.warning('this is warning message ...')
logging.error('this is error message ...')
logging.critical('this is critical message ...')
