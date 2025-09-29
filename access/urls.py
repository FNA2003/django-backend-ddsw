from django.urls import path
from .views import LogInAPI, RegisterAPI

# http://localhost:8000/api/users/...
urlpatterns = [
    path("login/", LogInAPI.as_view()),
    path("register/", RegisterAPI.as_view())
]