from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import ReviewViewSet

app_name = 'api'

router = DefaultRouter()

router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet,
                basename='review-list'
                )
router.register(r'titles/(?P<title_id>\d+)/reviews/?P<review_id>\d+/',
                ReviewViewSet,
                basename='reviews-details'
                )


urlpatterns = [
    path('', include(router.urls)),
]