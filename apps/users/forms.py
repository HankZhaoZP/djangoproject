# __author__ = 'HankZhao'
# __date__ = '2017/12/30 23:00'
# Description:用form实现登陆
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ForgetFrom(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ResetFrom(forms.Form):
    new_password = forms.CharField(required=True, min_length=5)
    sure_password = forms.CharField(required=True, min_length=5)
