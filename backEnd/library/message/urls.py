from django.urls import path

from message import views

urlpatterns = [
#登录注册模块 Login
#登录 LoginServlet
    path('LoginServlet/',views.LoginServlet),

]