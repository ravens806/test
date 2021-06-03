from os import name
from django.urls import path , include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.TopViews.as_view(),name = 'top'),
    path('login',views.Login.as_view(),name='login'), #Login 
    path('signup',views.SignUp.as_view(),name='signup'),#sgin_up
    path('logout',views.Logout.as_view(),name='logout'),#Logout
    path('signup_done',views.SignupDone.as_view(),name='signup_done'),#signup完了
    path('mypage/<int:pk>',views.Mypage.as_view(),name='mypage')#mypage
]