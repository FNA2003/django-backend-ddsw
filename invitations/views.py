from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from django.db.models import Q

from .models import Invitations, InvitationsEnum
from .serializers import InvitationsSerializer


""" NOTA: Para el acceso hacer:

    fetch('http://localhost:8000/api/invitations/list/', {
    method: 'GET',
    headers: {
        Authorization: 'Bearer ' + access
    }
    })
    .then((response) => response.json())  // Convertimos la respuesta a JSON
    .then((data) => console.log(data))    // Mostramos el JSON en consola
    .catch((error) => console.error('Error:', error)); // Por si hay errores
"""
class ListInvitationsAPI(APIView):
    permission_classes = [IsAuthenticated] # Solamente se puede acceder a estas vistas loggeado

    def get(self, request):
        usuario = request.user # Obtenemos el usuario autentificado

        # Hacemos una ÚNICA query para buscar las invitaciones pendientes
        invitaciones = Invitations.objects.filter(
            # Esta primera sub-query buscará a los usuarios que se les envió 
            # la invitación por mail pero no se les vinculó (no existía el usuario)
            Q(receiver_email=usuario.email, receiver_fk__isnull=True) |
            # Y, esta otra sub-query busca solamente las invitaciones especificadas a un usuario
            Q(receiver_email=usuario.email, receiver_fk=usuario.id),
            state=InvitationsEnum.PENDING
        )

        serializer = InvitationsSerializer(invitaciones, many=True)

        return Response({"data":serializer.data}, status=200)
    


""" Se espera un body como:

    {
        "emails": [
            "pepito@email.com",
            "hola@email.com"
        ]
    }
"""
class SendInvitationsAPI(APIView):
    #permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        datos = request.data.get("emails") # Se recibirá una lista de emails para invitar

        for email in datos:
            print(email)