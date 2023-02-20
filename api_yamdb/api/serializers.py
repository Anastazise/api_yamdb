from django.db.models import Avg
from rest_framework import serializers
from reviews.models import Category, Genre, Review, Title, User, Comment
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        )
        model = User
        read_only_field = ('role',)


class RegisterDataSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("username", "email")
        model = User


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        fields = ['id', 'text', 'author', 'score', 'pub_date']

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        if request.method == 'POST':
            if Review.objects.filter(title=title, author=author).exists():
                raise ValidationError('Отзыв уже написан вами')
        return data


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'slug', ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)

    def get_rating(self, obj):
        """
        Возвращает среднее значение рейтинга.
        """
        average_rating = obj.reviews.all().aggregate(
            Avg('score'))['score__avg']
        if average_rating is None:
            return None
        return int(average_rating)

    class Meta:
        model = Title
        fields = ['id',
                  'name',
                  'year',
                  'rating',
                  'description',
                  'category',
                  'genre', ]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'pub_date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        )
        model = User
        read_only_field = ('role',)
