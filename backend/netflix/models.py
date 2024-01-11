from django.db import models

# Create your models here.

class Cast(models.Model):
    show_id=models.CharField(max_length=100)
    cast=models.CharField(max_length=500)

class Country(models.Model):
    show_id=models.CharField(max_length=100)
    country=models.CharField(max_length=300)

class Data(models.Model):
    show_id=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    # date_added=models.CharField(max_length=15) # 2021-02-23
    release_year=models.PositiveSmallIntegerField()
    rating=models.CharField(max_length=150)
    # duration=models.CharField(max_length=15)

class Director(models.Model):
    show_id=models.CharField(max_length=100)
    director=models.CharField(max_length=300)

class Listed(models.Model):
    show_id=models.CharField(max_length=100)
    catalog=models.CharField(max_length=400)
"""
class Movies(models.Model):
    show_id=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    date_add=models.CharField(max_length=15)
    release_year=models.PositiveSmallIntegerField()
    rating=models.CharField(max_length=15)
    duration=models.CharField(max_length=15)
"""
class Netflix(models.Model):
    GENRE_CHOICES = (
        ('TV Show', 'TV Show'),
        ('Movie', 'Movie')
    )
    show_id=models.CharField(max_length=100)
    type=models.CharField(max_length=100, choices=GENRE_CHOICES)
    title=models.CharField(max_length=50)
    director=models.CharField(max_length=300)
    # we ignore cast-column
    duration=models.CharField(max_length=150, default='0')
"""
class Movie(models.Model):
    show_id=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    date_add=models.CharField(max_length=15)
    release_year=models.PositiveSmallIntegerField()
    rating=models.CharField(max_length=15)
"""
class Form(models.Model):
    show_id=models.CharField(max_length=100, null=False)
    title=models.CharField(max_length=500, null=False)
    type=models.CharField(max_length=100, null=False, default='TV show')
    director=models.CharField(max_length=300,default='None')
    cast=models.CharField(max_length=300, default='NAME')
    country=models.CharField(max_length=300, null=False)
    rating=models.CharField(max_length=150, null=False)
    duration=models.CharField(max_length=150, null=False) # duration/season
    release_year=models.PositiveSmallIntegerField(null=False)
    catalog=models.CharField(max_length=150, null=False)
    average_score=models.FloatField(null=True, default=0)
    score_count=models.IntegerField(null=True, default=0)
    comments=models.TextField(null=True)

class Comment(models.Model):
    show_id=models.CharField(max_length=100)
    comment=models.TextField()

class Ranking(models.Model):
    show_id=models.CharField(max_length=100)
    title=models.CharField(max_length=500, null=False)
    average_score=models.FloatField()

