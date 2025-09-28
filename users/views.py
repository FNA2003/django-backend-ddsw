from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Users
from .serializers import usersSerializer


# TODO: Autentificación y loggin

""" Retorna una lista de todos los usuarios de la bdd
    GET: .../api/users/
"""
class UsersListAPIView(APIView):
    def get(self, request):
        usr = Users.objects.all()
        serializer = usersSerializer(usr, many=True)

        return Response({"data":serializer.data}, status=200)

""" Ver información de un usuario, modificarla ó borrarla
    GET: .../api/users/{id_usuario}/
    PATCH: .../api/users/{id_usuario}/
    DELETE: .../api/users/{id_usuario}/
"""
class UserDetailAPIView(APIView):
    # permission_classes=[IsAuthenticated]

    def get(self, request, user_id):
        usuario = get_object_or_404(Users, user_id=user_id)
        serializer = usersSerializer(usuario)
        return Response({"data":serializer.data}, status=200)
        
    def patch(self, request, user_id):        
        usuario = get_object_or_404(Users, user_id=user_id)
        serializer = usersSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data}, status=200)
        
        return Response({"errors":serializer.errors}, status=400)

    def delete(self, request, user_id):        
        usuario = get_object_or_404(Users, user_id=user_id)
        usuario.delete()
        return Response({"message":"Usuario eliminado"}, status=200)
    

""" TODO: Loggeo de un usuario
    POST: .../api/users/login/
"""
class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data["user"]
        password = request.data["password"]

        raise Exception(NotImplemented)
    
""" Registrar un usuario
    POST: .../api/users/register/
"""
class UserRegisterAPIView(APIView):
    def post(self, request):
        user = request.data
        serializer = usersSerializer(data=user)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data}, status=200)
        
        return Response({"errors":serializer.errors}, status=400)