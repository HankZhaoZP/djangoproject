# -*- coding: utf-8 -*-
# @Time    : 2017/12/31 16:02
# @Author  : HankZhao
# @File    : email_send.py
# @Describe:
from apps.users.models import EmailVerifyRecord


def send_register_email(email,type=0):
    email_record = EmailVerifyRecord()
    random_str = ''

