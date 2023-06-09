from django.db import models

# Create your models here.
from django.db import models
from tatu.models import ServicePrice
from .admin import admin


class MasterCRM(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100, default=" ",null=False)
    surname = models.CharField(verbose_name="Фамилия", max_length=100,default="",null=False)
    tel = models.CharField(verbose_name="Номер телефона", max_length=100,default="+7",null=False)
    chart = models.CharField(verbose_name="График работы", max_length=100,default="пн/сб",null=False)

    def __str__(self):
        return self.name + " " + self.tel

    class Meta:
        verbose_name = "Мастера"
        verbose_name_plural = "Мастер"


class ClientCRM(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100, default=" ", null=False)
    surname = models.CharField(verbose_name="Фамилия", max_length=100, default="",null=False)
    tel = models.CharField(verbose_name="Номер телефона", max_length=100, default="+7",null=False)

    def __str__(self):
        try:
            return f"{self.name} {self.surname} -> {self.tel}"
        except:
            return f" Клиент №{self.pk}"

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиент"

class SupportCRM(models.Model):
    master = models.ForeignKey(MasterCRM, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(ClientCRM, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(ServicePrice, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        try:
            return self.master.__str__() + " -> "  + self.client.__str__() + " -> " + self.service.__str__()
        except:
            return f"Заявка №{self.pk}"
        finally:
            return f"Заявка №{self.pk}"

    class Meta:
        verbose_name = "Записи"
        verbose_name_plural = "Запись"


admin.site.register([SupportCRM,ClientCRM,MasterCRM])