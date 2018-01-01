# -*- coding: utf-8 -*-
# @Time    : 2017/12/31 16:02
# @Author  : HankZhao
# @File    : email_send.py
# @Describe:生成随机验证码和发送激活邮件
from django.core.mail import send_mail

from apps.users.models import EmailVerifyRecord
from djangoproject.settings import EMAIL_FROM

from random import Random


def send_type_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)

    email_record.email = email
    email_record.code = code
    email_record.send_type = send_type
    email_record.save()

    email_title = '邮件标题'
    email_body = '邮件内容'

    if send_type == "register":
        email_title = "账户激活邮件"
        email_body = "请点击链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
    elif send_type == "forget":
        email_title = "找回密码邮件"
        email_body = "请点击链接更改你的账户密码：http://127.0.0.1:8000/reset/{0}".format(code)

    return send_email(email_title, email_body, email)


def random_str(randomlength=8):
    code = ''
    charts = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    length = len(charts) - 1
    random = Random()
    for i in range(randomlength):
        code += charts[random.randint(0, length)]
    return code


def send_email(email_title, email_body, email_address):
    send_status = send_mail(
        email_title,
        email_body,
        EMAIL_FROM,
        [email_address],
        fail_silently='False'
    )
    return send_status


