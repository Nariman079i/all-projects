from rest_framework.generics import CreateAPIView
from support.api.serializers import *


class SupportCreateAPI(CreateAPIView):
    serializer_class = SupportSerializer
    queryset = Support.objects.all()