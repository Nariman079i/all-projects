from django.db import models
from images.admin import admin


# Create your models here.
class Image(models.Model):
    title = models.CharField("Наименование", max_length=255, null=True, blank=True)
    image = models.ImageField("Изображение", max_length=255, null=True, blank=True, upload_to='images/')
    alt = models.CharField("Альтернативный текст", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.image.name


admin.site.register(Image)