from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Titles, Genres, Categories
from .serializers import TitlesSerializer, GenresSerializer, CategoriesSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend



class CategoriesViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ('name',)
    lookup_field = 'slug' 


class GenresViewset(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ('name',)
    lookup_field = 'slug' 

class TitlesViewset(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    pagination_class = PageNumberPagination