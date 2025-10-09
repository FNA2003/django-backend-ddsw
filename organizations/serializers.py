from rest_framework.serializers import ModelSerializer
from .models import Organizations

class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organizations
        fields = "__all__"