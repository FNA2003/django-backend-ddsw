from rest_framework.serializers import ModelSerializer

from organizations.serializers import OrganizationSerializer
from access.serializers import UsersSerializer

from .models import Invitations


class InvitationsSerializer(ModelSerializer):
    organization_fk = OrganizationSerializer(read_only=True)
    sender_fk = UsersSerializer(read_only=True)
    class Meta():
        model=Invitations
        fields="__all__"