from rest_framework.serializers import *
from .models import *


class CRMServiceSeializer(ModelSerializer):
    img = HiddenField(default=None)

    class Meta:
        model = CRMService
        fields = "__all__"


class CRMCustomerSeializer(ModelSerializer):
    class Meta:
        model = CRMCustomer
        fields = "__all__"


class CRMMasterSeializer(ModelSerializer):
    class Meta:
        model = CRMMaster
        fields = "__all__"



class CRMSessionSeializer(ModelSerializer):
    class Meta:
        model = CRMSession
        fields = "__all__"