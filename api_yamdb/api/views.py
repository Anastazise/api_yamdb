from rest_framework import viewsets, permissions
from api.permissions import IsAuthorOrStaff
from api.serializers import ReviewSerializer
from reviews.models import Review


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
