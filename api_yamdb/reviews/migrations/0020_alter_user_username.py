# Generated by Django 3.2 on 2023-02-19 08:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0019_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator('\\w.@+-]+\\z', message='Введите корректное username')], verbose_name='Имя пользователя'),
        ),
    ]
