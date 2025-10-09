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

    def create(self, validated_data):
        request = self.context.get('request')
        organization = request.user.organization_fk
        sender = request.user

        return Invitations.objects.create(
            organization_fk=organization,
            sender_fk=sender,
            **validated_data
        )