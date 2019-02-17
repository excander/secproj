from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users_all, name='users_all'),
    path('id=<user_id>/', views.user_detail, name='user_detail'), #by-id?id=
    path('login=<str:user_login>/', views.user_detail_by_login, name='user_detail_by_login'), #by-login?login=

]