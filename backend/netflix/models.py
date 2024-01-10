from django.db import models

# Create your models here.


class Cast(models.Model):
    show_id = models.CharField(max_length=10)
    cast = models.CharField(max_length=50)


class Country(models.Model):
    show_id = models.CharField(max_length=10)
    country = models.CharField(max_length=30)


class Data(models.Model):
    show_id = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    # date_added=models.CharField(max_length=15) # 2021-02-23
    release_year = models.PositiveSmallIntegerField()
    rating = models.CharField(max_length=15)
    # duration=models.CharField(max_length=15)


class Director(models.Model):
    show_id = models.CharField(max_length=10)
    director = models.CharField(max_length=30)


class Listed(models.Model):
    show_id = models.CharField(max_length=10)
    catalog = models.CharField(max_length=40)


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
    show_id = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=30)
    # we ignore cast-column
    duration = models.CharField(max_length=15, default='0')


"""
class Movie(models.Model):
    show_id=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    date_add=models.CharField(max_length=15)
    release_year=models.PositiveSmallIntegerField()
    rating=models.CharField(max_length=15)
"""


class Form(models.Model):
    show_id = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=10, null=False, default='TV show')
    director = models.CharField(max_length=30, default='None')
    country = models.CharField(max_length=30, null=False)
    rating = models.CharField(max_length=15, null=False)
    duration = models.CharField(max_length=15, null=False)  # duration/season
    release_year = models.PositiveSmallIntegerField(null=False)
    catalog = models.CharField(max_length=15, null=False)
    average_score = models.FloatField(null=True)
    score_count = models.IntegerField(null=True)
    comments = models.TextField(null=True)


class Comment(models.Model):
    show_id = models.CharField(max_length=10)
    comment = models.TextField()
