# Generated by Django 4.2 on 2023-04-30 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0002_alter_category_options_alter_item_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('tel', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
            ],
            options={
                'verbose_name': 'Заявки',
                'verbose_name_plural': 'Заявка',
            },
        ),
    ]
