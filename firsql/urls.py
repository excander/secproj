from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users_all, name='users_all'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),

]