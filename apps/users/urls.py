# __author__ = 'HankZhao'
# __date__ = '2017/12/30 20:42'
# Description:定义登陆和注册功能相关的url

from django.conf.urls import url

from apps.users.views import LoginView, RegisterView, ActiveUserView, ForgetPasswordView, ResetView, ResetPasswordView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='active'),
    url(r'^forget/$', ForgetPasswordView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name='reset'),
    url(r'^reset/$', ResetPasswordView.as_view(), name='reset_password')
]