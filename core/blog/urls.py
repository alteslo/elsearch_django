from django.urls import path, include
from rest_framework import routers

from blog.views import UserViewSet, CategoryViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('category', CategoryViewSet)
router.register('article', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
