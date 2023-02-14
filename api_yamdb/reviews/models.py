from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200)

    def __str__(self):
        return self.title


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200)
    year = models.IntegerField(
        verbose_name='Год выпуска'
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=2000
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория',
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр',
    )

    def __str__(self):
        return self.title
