from rest_framework.serializers import ModelSerializer
from support.models import *


class SupportSerializer(ModelSerializer):
    class Meta:
        model = Support
        fields = "__all__"
