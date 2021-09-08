from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet, basename='authors')
router.register(r'tags', views.TagViewSet, basename='tags')
router.register(r'posts', views.PostViewSet, basename='post')
urlpatterns = [
    path('', include(router.urls)),
]
