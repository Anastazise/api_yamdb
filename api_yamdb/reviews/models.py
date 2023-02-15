from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200)

    slug = models.SlugField(
        verbose_name='slug',
        max_length=200,
        null=True
    )

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200)

    slug = models.SlugField(
        verbose_name='slug',
        max_length=200,
        null=True
    )

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


class Review(models.Model):
    text = models.TextField(
        verbose_name='Текст отзыва',
        max_length=256
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    score = models.SmallIntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        unique_together = ('author', 'title')

    def __str__(self):
        return self.text[:10]


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Текст коментария',
        max_length=256
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Произведение'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.text[:10]
