from django.db import models

# Create your models here.
from django.db import models
from tatu.models import ServicePrice
from .admin import admin


class MasterCRM(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100, default=" ")
    surname = models.CharField(verbose_name="Фамилия", max_length=100,default="")
    tel = models.CharField(verbose_name="Номер телефона", max_length=100,default="+7")
    chart = models.CharField(verbose_name="График работы", max_length=100,default="пн/сб")

    def __str__(self):
        return self.name + " " + self.tel

    class Meta:
        verbose_name = "Мастера"
        verbose_name_plural = "Мастер"


class ClientCRM(models.Model):
    name = models.CharField(verbose_name="", max_length=100, default=" ")
    surname = models.CharField(verbose_name="Фамилия", max_length=100, default="")
    tel = models.CharField(verbose_name="Номер телефона", max_length=100, default="+7")

    def __str__(self):
        return self.name + " " + self.tel

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиент"
class SupportCRM(models.Model):
    master = models.ForeignKey(MasterCRM, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(ClientCRM, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(ServicePrice, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.master.__str__() + " -> "  + self.client + " -> " + self.service.__str__()

    class Meta:
        verbose_name = "Записи"
        verbose_name_plural = "Запись"


admin.site.register([SupportCRM,ClientCRM,MasterCRM])