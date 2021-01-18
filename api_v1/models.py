from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=40, unique=True)



class Genres(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=40, unique=True)

Rating_CHOICES = (
    (None, 'No rating'),   
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)

class Titles(models.Model):
    name = models.CharField(max_length=200, unique=True)
    year = models.DateTimeField("Дата создания", auto_now_add=True, db_index=True)
    description = models.TextField()
    rating = models.IntegerField(choices=Rating_CHOICES, default=None)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="titles")
    genre = models.ForeignKey(Genres, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="titles")