# Generated by Django 4.2 on 2023-05-23 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRMCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('tel', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='CRMMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('tel', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона')),
                ('salary', models.IntegerField(blank=True, null=True, verbose_name='Зарплата')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='CRMService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Изображение')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('direct_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Полное описание')),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='CRMSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_session', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.crmcustomer')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.crmmaster')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.crmservice')),
            ],
            options={
                'verbose_name': 'Сеанс',
                'verbose_name_plural': 'Сеансы',
            },
        ),
    ]
