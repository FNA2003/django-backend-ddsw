from django.urls import path
from .views import ListInvitationsAPI

# http://localhost:8000/api/invitations/...
urlpatterns = [
    path("list/", ListInvitationsAPI.as_view())

    # Uno para enviar las invitaciones path("send/"
    # Otro para manejar aceptarlas o rechazarlas con post o delete path("handle/"
]