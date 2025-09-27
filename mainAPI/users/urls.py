from django.urls import path

from .views import *


urlpatterns = [
    path("", UsersListAPIView.as_view()),

    path("<int:id_usuario>/",UserDetailAPIView.as_view())
]