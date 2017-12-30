# __author__ = 'HankZhao'
# __date__ = '2017/12/30 20:42'
# Description:定义登陆和注册功能相关的url

from django.conf.urls import url

from apps.users.views import LoginView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login')
]