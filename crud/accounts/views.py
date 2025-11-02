from django.shortcuts import render
from django import forms
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()  # 🔑 Campo de captcha

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "captcha")

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

class LogoutMessageView(TemplateView):
    template_name = 'accounts/logoutMessage.html'