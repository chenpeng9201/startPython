#!/usr/bin/env python
# coding=utf-8
import logging
from common import except_helper, mail_helper
import traceback


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
handler = logging.FileHandler('../log/applog.log')
handler.setLevel(logging.DEBUG)
handler.encoding = 'GBK'
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def log_info(msg):
    logger.info(msg)


def log_debug(msg):
    logger.debug(msg)


def log_error(msg, is_send_mail=True):
    if traceback:
        msg = msg + '\n' + traceback.format_exc() + '\n'
    # 获取程序当前运行的堆栈信息
    detailtrace = except_helper.detailtrace()
    msg = msg + '程序调用堆栈的日志：' + detailtrace + '\n'
    logger.error(msg)

    # 发送邮件通知相关人员
    if is_send_mail:
        info = mail_helper.send_error_mail(context=msg)
        if info: logging.info(info)



