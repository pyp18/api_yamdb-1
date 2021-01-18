from django.urls import include, path
from .views import CategoriesViewset, GenresViewset, TitlesViewset
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'categories', CategoriesViewset, basename='categories')
router.register(r'genres', GenresViewset, basename='genres')
router.register(r'titles', TitlesViewset, basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),

]
