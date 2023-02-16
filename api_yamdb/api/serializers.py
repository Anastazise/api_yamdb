from rest_framework import serializers
from reviews.models import Title, Review, User, Comment
from django.db.models import Avg


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        """
        Возвращает среднее значение рейтинга.
        """
        average_rating = obj.reviews.all().aggregate(Avg('score'))['score__avg']
        if average_rating is None:
            return 0
        return int(average_rating)

    class Meta:
        model = Title
        fields = ['name', 'year', 'rating', 'description', ]


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        fields = ['id', 'text', 'author', 'score', 'pub_date', ]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'pub_date']
