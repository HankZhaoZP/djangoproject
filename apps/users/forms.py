# __author__ = 'HankZhao'
# __date__ = '2017/12/30 23:00'
# Description:用form实现登陆
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)