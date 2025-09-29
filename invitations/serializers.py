from rest_framework.serializers import ModelSerializer

from .models import Invitations


class InvitationsSerializer(ModelSerializer):
    class Meta():
        model=Invitations
        fields="__all__"