from django.db import models
from items.models import Item
from support.admin import admin

class Support(models.Model):
    surname = models.CharField("Фамилия", max_length=255, null=True, blank=True)
    name = models.CharField("Имя", max_length=255, null=True, blank=True)
    patronymic = models.CharField("Отчество", max_length=255, null=True, blank=True)
    tel = models.CharField("Номер телефона", max_length=255, null=True, blank=True)
    address = models.CharField("Адрес", max_length=255, null=True, blank=True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE,verbose_name="Товар")

    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = "Заявка"

    def __str__(self):
        return f"{self.surname} {self.name} {self.tel}"


admin.site.register(Support)