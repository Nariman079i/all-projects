from django.db import models
from items.models import Category, Item
from items.admin import admin


class Banner(models.Model):
    img = models.ImageField("Изображение", null=True, blank=True, upload_to='img/')
    title = models.CharField("Наименование", max_length=255, null=True, blank=True)
    description = models.TextField("Описание", null=True, blank=True)
    url = models.URLField("Ссылка", null=True, blank=True)

    class Meta:
        verbose_name = "Банеры"
        verbose_name_plural = "Банер"

    def __str__(self):
        return f"{self.pk} {self.title}"


class Page(models.Model):
    title = models.CharField("Наименование", max_length=255, null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    banner = models.ForeignKey(Banner,on_delete=models.SET_NULL,null=True, blank=True)
    items = models.ManyToManyField(Item, blank=True)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return f"Страница -> {self.title}"


admin.site.register([Banner, Page])
