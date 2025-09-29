from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

from .serializers import UsersSerializer


""" NOTA: Los JWT tienen la siguiente forma:
        {
        "access": "eyJ0eXAiOiJKV1QiLCJh... (token JWT en sí)",
        "refresh": "eyJ0eXAiOiJKV1QiLCJh... (token de para 'recargar' sesión)"
        }
"""

# Maneja la autenticación y el retorno del JWT
class LogInAPI(APIView):
    def post(self, request):
        mail = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=mail, password=password)
        if user != None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access":str(refresh.access_token),
                "refresh":str(refresh)
            }, status=200)
        else:
            return Response({"error":"Credenciales inválidas"}, status=400)


# Maneja el registro y, si se pudo registrar, retorna un JWT para la sesión
class RegisterAPI(APIView):
    def post(self, request):
        serial = UsersSerializer(data=request.data)
        if not serial.is_valid():
            return Response({"error":serial.errors}, status=400)
        
        user = serial.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            "access":str(refresh.access_token),
            "refresh":str(refresh)
        }, status=200)



""" 
from rest_framework.permissions import IsAuthenticated

class MiVista(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # Este es el usuario autenticado por el token
        return Response({"email": user.email})

    {
        "username":"El gran pepo",
        "first_name":"Pepe",
        "last_name":"Argento",
        "email":"pepe@ejemplo.com",
        "password":"123"
    }
"""