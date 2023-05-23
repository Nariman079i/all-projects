# Generated by Django 4.1.6 on 2023-04-18 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0004_alter_feedback_message_alter_service_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='page',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Дополнительное описание'),
        ),
        migrations.AlterField(
            model_name='page',
            name='history_description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание истории'),
        ),
        migrations.AlterField(
            model_name='page',
            name='main_description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Главное описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Полное описание'),
        ),
    ]