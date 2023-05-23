from pages.api.serializers import *
from rest_framework.generics import RetrieveAPIView


class PageViewAPI(RetrieveAPIView):
    serializer_class = PageSerializer
    queryset = Page.objects.all()

    def get_object(self):
        return Page.objects.all().first()