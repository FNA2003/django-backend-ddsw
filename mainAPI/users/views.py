from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Users
from .serializers import usersSerializer


# TODO: Permisos e inicio de sesión

""" Retorna una lista de todos los usuarios de la bdd
    GET: .../api/users/
"""
class UsersListAPIView(APIView):
    def get(self, request):
        usr = Users.objects.all()
        serializer = usersSerializer(usr)

        return Response({"data":serializer.data}, status=200)

""" Ver información de un usuario, modificarla ó borrarla
    GET: .../api/users/{id_usuario}/
    PATCH: .../api/users/{id_usuario}/
    DELETE: .../api/users/{id_usuario}/
"""
class UserDetailAPIView(APIView):
    def get(self, request, id_usuario):
        pass
    def patch(self, request, id_usuario):
        pass
    def delete(self, request, id_usuario):
        pass