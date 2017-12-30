from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile
from .forms import LoginForm


class CustomBackennd(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", context={})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            user_password = request.POST.get("password", "")
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html", context={
                    'msg': '用户名或密码错误'
                })
        else:
            return render(request, "login.html", context={
                'login_form': login_form
            })


# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username", "")
#         user_password = request.POST.get("password", "")
#         user = authenticate(username=user_name, password=user_password)
#
#         if user is not None:
#             login(request, user)
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html", context={})
#
#     elif request.method == "GET":
#         return render(request,"login.html",context={})
