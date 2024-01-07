import django
from django.db import models
# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    rating = models.TextField(default="name")
    cast = models.TextField(default="name")
    duration = models.DurationField(default="name")
    season = models.CharField(max_length=30)
    release_year = models.DateField(auto_now_add=True)
    catalog = models.TextField(default="name")
    average_score = models.FloatField()
    score_counts = models.DecimalField(max_digits=2, decimal_places=0)
    comments = models.TextField(default="name")
    comments_date = models.DateField(auto_now=True)

    class Meta:
        db_table = "movie"
