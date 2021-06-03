from django import forms
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignObject
from django.shortcuts import render , redirect
from django.views.generic import TemplateView ,CreateView
from django.contrib.auth.views import LoginView , LogoutView
from django.views.generic.detail import DetailView 
from .forms import LoginForm , Signform
from django.contrib.auth import get_user_model ,login
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
class TopViews(TemplateView):
    template_name = "top.html"

class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

class Logout(LogoutView):
    template_name = 'logout.html'

class SignUp(CreateView):
    template_name = "signup.html"
    form_class = Signform

    def form_valid(self, form):
        user = form.save()
        return redirect('top')


class SignupDone(TemplateView):
        template_name = 'signup_done.html'

class MypageLink(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk']

class Mypage(MypageLink,DetailView):
    model = User 
    template_name = 'mypage.html'