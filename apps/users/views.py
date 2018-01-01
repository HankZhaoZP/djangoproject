from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm
from .utils.email_send import send_register_email


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# Create your views here.


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()

        return render(request, 'login.html', context={})

    def post(self, request):
        pass


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", context={
            'register_form': register_form
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")

            user_porfile = UserProfile()
            user_porfile.username = email
            user_porfile.email = email
            user_porfile.password = make_password(password)
            user_porfile.is_active = False
            user_porfile.save()

            send_register_email(email, "register")
            return render(request, "login.html", context={})
        else:
            return render(request, "register.html", context={
                'register_form': register_form
            })


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
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", context={
                        'msg': '账户未激活'
                    })
            else:
                return render(request, "login.html", context={
                    'msg': '用户名或密码错误'
                })
        else:
            return render(request, "login.html", context={
                'login_form': login_form
            })

