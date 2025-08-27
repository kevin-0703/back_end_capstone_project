from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet, RegisterView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('cinemate/register/', RegisterView.as_view(), name='register'),
]