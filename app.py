import logging
import os
from logging import handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "http://182.92.81.159"
HEADERS = {"Content-Type":"application/json"}
EMP_ID = 0


def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    filename = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename, when='M', interval=1, backupCount=7)
    # 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(fh)
    logger.addHandler(sh)
