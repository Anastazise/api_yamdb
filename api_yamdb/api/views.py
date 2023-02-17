from api.permissions import IsAuthorOrStaff, IsStaffOrReadOnly
from api.serializers import (CategorySerializer, GenreSerializer,
                             ReviewSerializer, TitleSerializer, CommentSerializer)
from rest_framework import permissions, viewsets
from reviews.models import Category, Genre, Review, Title, Comment



class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action == 'partial_update' or self.action == 'delete':
            return (IsAuthorOrStaff(),)
        return super().get_permissions()

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        new_queryset = Review.objects.filter(title=title_id)
        return new_queryset

    def perform_create(self, serializer):
        title_id = self.kwargs.get("title_id")
        serializer.save(author=self.request.user, title_id=int(title_id))


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = (IsStaffOrReadOnly,)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsStaffOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action == 'partial_update' or self.action == 'delete':
            return (IsAuthorOrStaff(),)
        return super().get_permissions()

    def get_queryset(self):
        review_id = self.kwargs.get("review_id")
        new_queryset = Comment.objects.filter(review=review_id)
        return new_queryset

    def perform_create(self, serializer):
        review_id = self.kwargs.get("review_id")
        serializer.save(author=self.request.user, review_id=int(review_id))
