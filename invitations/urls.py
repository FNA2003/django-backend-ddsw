from django.urls import path
from .views import ListInvitationsAPI, SendInvitationsAPI, HandleInvitation

# http://localhost:8000/api/invitations/...
urlpatterns = [
    path("list/", ListInvitationsAPI.as_view()),

    path("send/", SendInvitationsAPI.as_view()),

    path("handle/<int:id>/", HandleInvitation.as_view()),
]