from items.models import Category, Item
from images.models import Image
from rest_framework.serializers import HyperlinkedModelSerializer,ModelSerializer


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'img', 'url', 'slug')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ItemSerializer(HyperlinkedModelSerializer):
    image_list = ImageSerializer(many=True)
    category = CategorySerializer(many=False)

    class Meta:
        model = Item
        fields = ('id', 'title', 'img', 'url', 'description', 'price','count','image_list','category')
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }

