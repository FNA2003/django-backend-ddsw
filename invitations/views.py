from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from django.db.models import Q

from .models import Invitations, InvitationsEnum
from .serializers import InvitationsSerializer
from access.models import Users


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
        if usuario.organization_fk:
            return Response({"errors":"Ya perteneces a una organización"}, status=400)

        # Hacemos una query para buscar las invitaciones pendientes
        invitaciones = Invitations.objects.filter(
            receiver_email=usuario.email,
            state=InvitationsEnum.PENDING
        )

        serializer = InvitationsSerializer(invitaciones, many=True)

        return Response({"data":serializer.data}, status=200)
    


""" Se espera un request como:

    fetch('http://localhost:8000/api/invitations/send/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access
    },
    body: JSON.stringify({
        emails: [
            "franco@email.com", 
            "ejemplo@email.com", 
            "pepe@email.com",
            "no_existo@email.com"
        ]
    })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error:', error));
"""
class SendInvitationsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        datos = request.data # Se recibirá una lista de emails para invitar

        # Acá verificamos si pertenece a una organización, si no es así, no puede invitar a nadie
        # TODO: Si se agregarán permisos, se deberá verificar sobre los permisos directamente
        if request.user.organization_fk == None:
            return Response({"error":"Usuario sin organización"}, status=400)

        # Preparamos los objetos "Invitations"
        invitaciones_data = []

        for email in datos:
            if email != request.user.email:
                invitaciones_data.append({
                    "receiver_email": email
                    # No incluimos sender_fk ni organization_fk aquí
                })

        # Pasamos el contexto con el request para que el serializer pueda acceder al usuario
        # NOTA: Esto se hace por que el sender_fk y organization_fk son de lectura unicamente y se deben manejar en la clase
        serializer = InvitationsSerializer(data=invitaciones_data, many=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Invitaciones enviadas"}, status=200)
        else:
            return Response({"error":serializer.errors}, status=400)
