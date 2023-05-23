from django.db import models
from images.models import Image
from images.admin import admin


class Category(models.Model):
    title = models.CharField("Наименование", max_length=255, null=True, blank=True)
    img = models.ImageField("Изображение", null=True, blank=True, upload_to="items/img/")
    slug = models.SlugField("Ссылка", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категория"

    def __str__(self):
        return f"{self.pk} {self.title}"


class Item(models.Model):
    title = models.CharField("Наименование", max_length=255, null=True, blank=True)
    description = models.TextField("Описание", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="item_category")
    img = models.ImageField("Изображение", null=True, blank=True, upload_to="items/img/")
    price = models.IntegerField("Стоимость", null=True, blank=True)
    image_list = models.ManyToManyField(Image, blank=True)
    count = models.IntegerField("Количество", null=True, blank=True)

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товар"

    def __str__(self):
        return f"{self.pk} {self.title}"

admin.site.register([Category, Item])