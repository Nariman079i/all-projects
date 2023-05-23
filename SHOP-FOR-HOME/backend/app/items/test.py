from PIL import Image
from django.db.models import QuerySet
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from items.models import Category
from support.models import *


class SupportTest(APITestCase):
    def setUp(self):
        self.url = reverse('support-create')
        self.image = Image.open(r'C:\Users\1\Desktop\test.png')
        self.image.name = "test"
        self.image.format = "PNG"

        self.item = Item.objects.create(
            title="Hello",
            price=10000
        )


class ItemsTest(APITestCase):
    def test_items_create(self):
        Category.objects.create(title="category")
        item = Item.objects.create(
            title="title",
            category_id=1
        )
        self.assertEqual(item.category.title , 'category')
        self.assertEqual(item.title,Item(pk=1,title='title').title)
