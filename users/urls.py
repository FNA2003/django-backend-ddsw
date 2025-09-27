from django.urls import path

from .views import *


urlpatterns = [
    path("", UsersListAPIView.as_view()),

    path("<int:user_id>/",UserDetailAPIView.as_view()),

    path("login/",UserLoginAPIView.as_view()),

    path("register/",UserRegisterAPIView.as_view()),
]