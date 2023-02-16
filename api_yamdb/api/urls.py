from api.views import (CategoryViewSet, GenreViewSet, ReviewViewSet,
                       TitleViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()

router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet,
                basename='review-list'
                )
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)',
                ReviewViewSet,
                basename='reviews-details'
                )
router.register(r'titles', TitleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
