# Generated by Django 4.1.6 on 2023-04-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True, verbose_name='Наименование')),
                ('surname', models.CharField(blank=True, max_length=60, null=True, verbose_name='Фамилия')),
                ('name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Имя')),
                ('message', models.CharField(blank=True, max_length=60, null=True, verbose_name='Сообщение')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзыв',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True, verbose_name='Наименование')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Изображение')),
                ('alt', models.CharField(blank=True, max_length=60, null=True, verbose_name='Альтернативный текст')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображение',
            },
        ),
        migrations.CreateModel(
            name='ServicePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True, verbose_name='Наименование')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуга',
            },
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Имя')),
                ('tel', models.CharField(blank=True, max_length=30, null=True, verbose_name='Телефон')),
                ('message', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Заявки',
                'verbose_name_plural': 'Заявка',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True, verbose_name='Наименование')),
                ('direct_description', models.CharField(blank=True, max_length=60, null=True, verbose_name='Краткое описание')),
                ('description', models.CharField(blank=True, max_length=60, null=True, verbose_name='Полное описание')),
                ('images', models.ManyToManyField(blank=True, related_name='images', to='salon.image')),
                ('price_list', models.ManyToManyField(blank=True, related_name='services', to='salon.serviceprice')),
            ],
            options={
                'verbose_name': 'Категории услуг',
                'verbose_name_plural': 'Категория услуги',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Главный заголовок')),
                ('main_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Главное описание')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительный заголовок')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное описание')),
                ('history_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок истории')),
                ('history_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание истории')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на страницу описания')),
                ('feedback', models.ManyToManyField(blank=True, to='salon.feedback', verbose_name='Отзывы')),
            ],
            options={
                'verbose_name': 'Страницы',
                'verbose_name_plural': 'Страница',
            },
        ),
    ]
