from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetFrom, ResetFrom
from .utils.email_send import send_type_email


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
        else:
            return render(request, 'active_fail.html', context={})

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

            if UserProfile.objects.filter(email=email):
                return render(request, "register.html", context={
                    'msg': '该账户已被注册',
                    'register_form': register_form
                })
            else:
                user_profile = UserProfile()
                user_profile.username = email
                user_profile.email = email
                user_profile.password = make_password(password)
                user_profile.is_active = False
                user_profile.save()

                send_type_email(email, "register")
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


class ForgetPasswordView(View):
    def get(self, request):
        forget_form = ForgetFrom()
        return render(request, 'forgetpwd.html', context={
            'forget_form': forget_form
        })

    def post(self, request):
        forget_form = ForgetFrom(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")

            if UserProfile.objects.filter(email=email):
                if send_type_email(email, "forget"):
                    return render(request, 'send_success.html', context={})
            else:
                return render(request, "forgetpwd.html", context={
                    'msg': '该账户不存在',
                    'forget_form': forget_form
                })
        else:
            return render(request, 'forgetpwd.html', context={
                'forget_form': forget_form
            })


class ResetView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', context={
                    "email": email
                })
        else:
            return render(request, 'reset_fail.html', context={})


class ResetPasswordView(View):
    def post(self, request):
        reset_form = ResetFrom(request.POST)
        if reset_form.is_valid():
            email = request.get("email", "")
            new_password = request.get("new_password")
            sure_password = request.get("sure_password")

            if new_password != sure_password:
                return render(request, 'password_reset.html', context={
                    "email": email,
                    "msg": "密码不一致"
                })
            else:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(new_password)
                user.save()
                return render(request, "login.html", context={})

        else:
            email = request.get("email", "")
            return render(request, 'password_reset.html', context={
                "email": email,
                'reset_form': reset_form
            })
