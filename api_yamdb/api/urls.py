from api.views import (CategoryViewSet, GenreViewSet, ReviewViewSet,
                       TitleViewSet, CommentViewSet, UserViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import register, get_jwt_token

app_name = 'api'

router = DefaultRouter()

router.register(r'titles', TitleViewSet)

router.register(r'categories/(?P<slug>\w+)', CategoryViewSet)
router.register(r'genres/(?P<slug>\w+)', GenreViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                r'/comments', CommentViewSet, basename='comments')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', register, name='register'),
    path('auth/token/', get_jwt_token, name='token')
]
