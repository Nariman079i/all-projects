from rest_framework.serializers import ModelSerializer
from items.api.seriazlisers import *
from pages.models import Banner,Page


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class PageSerializer(ModelSerializer):
    category = CategorySerializer(many=True)
    banner = BannerSerializer(many=False)
    items = ItemSerializer(many=True)

    class Meta:
        model = Page
        fields = "__all__"