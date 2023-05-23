# Generated by Django 4.2 on 2023-04-30 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0002_alter_category_options_alter_item_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Изображение')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Банеры',
                'verbose_name_plural': 'Банер',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('banner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.banner')),
                ('category', models.ManyToManyField(blank=True, to='items.category')),
                ('items', models.ManyToManyField(blank=True, to='items.item')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]