from rest_framework.views import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class CRMCustomerAPIView(ModelViewSet):
    serializer_class = CRMCustomerSeializer
    queryset = CRMCustomer.objects.all()


class CRMServiceAPIView(ModelViewSet):
    serializer_class = CRMServiceSeializer
    queryset = CRMService.objects.all()


class CRMSessionAPIView(ModelViewSet):
    serializer_class = CRMSessionSeializer
    queryset = CRMSession.objects.all()


class CRMMasterAPIView(ModelViewSet):
    serializer_class = CRMMasterSeializer
    queryset = CRMMaster.objects.all()



