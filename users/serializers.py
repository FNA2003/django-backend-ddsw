from rest_framework import serializers
from .models import Users


class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["user_id", "name", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True} # Solamente se aceptará la contraseña, no se mostrará
        }
    
    def create(self, validated_data):
        user = Users(
            name=validated_data["name"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user