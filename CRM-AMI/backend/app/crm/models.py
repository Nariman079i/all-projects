from asgiref.sync import async_to_sync


from django.db.models import *
from django.db import models
from .admin import admin






class CRMService(models.Model):
    img = models.ImageField("Изображение",upload_to='img/',null=True,blank=True)
    title = models.CharField("Наименование", null=True, blank=True,max_length=255)
    direct_description = models.CharField("Краткое описание", null=True, blank=True,max_length=255)
    description = models.TextField("Полное описание", null=True, blank=True,max_length=1000)
    price = models.IntegerField()

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title


class CRMMaster(models.Model):
    surname = CharField("Фамилия", null=True, blank=True, max_length=255)
    name = CharField("Имя", null=True, blank=True, max_length=255)
    patronymic = CharField("Отчество", null=True, blank=True, max_length=255)

    tel = CharField("Номер телефона", null=True, blank=True, max_length=255)

    salary = IntegerField("Зарплата", null=True, blank=True)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.name


class CRMCustomer(Model):
    surname = CharField("Фамилия", null=True, blank=True, max_length=255)
    name = CharField("Имя", null=True, blank=True, max_length=255)
    patronymic = CharField("Отчество", null=True, blank=True, max_length=255)

    tel = CharField("Номер телефона", null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.surname} {self.name} {self.tel}"


class CRMSession(Model):
    customer = ForeignKey(CRMCustomer, on_delete=CASCADE)
    master = ForeignKey(CRMMaster, on_delete=CASCADE)
    service = ForeignKey(CRMService, on_delete=CASCADE)
    date_session = DateTimeField()

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"

    def __str__(self):
        return self.master.__str__() + " -> " + self.customer.__str__() + " -> " + self.service.__str__()


admin.site.register([CRMService,CRMSession,CRMCustomer,CRMMaster])
