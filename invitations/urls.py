from django.urls import path
from .views import ListInvitationsAPI, SendInvitationsAPI

# http://localhost:8000/api/invitations/...
urlpatterns = [
    path("list/", ListInvitationsAPI.as_view()),

    path("send/", SendInvitationsAPI.as_view())

    # TODO: Otro path para manejar aceptarlas o rechazarlas con post o delete path("handle/"
]