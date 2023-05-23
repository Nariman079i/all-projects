from django.db.models import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import request

from support.services import send_telegram_message
from support.models import *


@receiver(post_save,sender=Support)
def create_profile(instance:Support, created, **kwargs):
    if created:
        item = instance.item
        message = f"""*Заказ №{instance.pk}*\nФИО: {instance.surname} {instance.name} {instance.patronymic}\nТелефон: {instance.tel}\nАдрес: {instance.address}
\n*Информация о товаре:* \nНазвание: {item.title}\nCтоимость: {item.price}p"""

        send_telegram_message(message)
