from django.db import models

# Create your models here.

class Cast(models.Model):
    show_id=models.CharField(max_length=10)
    cast=models.CharField(max_length=50)

class Country(models.Model):
    show_id=models.CharField(max_length=10)
    country=models.CharField(max_length=30)

class Data(models.Model):
    show_id=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    date_added=models.CharField(max_length=15)
    release_year=models.PositiveSmallIntegerField()
    rating=models.CharField(max_length=15)
    # duration=models.CharField(max_length=15)

class Director(models.Model):
    show_id=models.CharField(max_length=10)
    director=models.CharField(max_length=30)

class Listed(models.Model):
    show_id=models.CharField(max_length=10)
    listed_in=models.CharField(max_length=40)

class Movies(models.Model):
    show_id=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    date_add=models.CharField(max_length=15)
    release_year=models.PositiveSmallIntegerField()
    rating=models.CharField(max_length=15)
    duration=models.CharField(max_length=15)

class Netflix(models.Model):
    show_id=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    title=models.CharField(max_length=50)
    director=models.CharField(max_length=30)
    # we ignore cast-column
    duration=models.CharField(max_length=15)

class Movies(models.Model):
    show_id=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    date_add=models.CharField(max_length=15)
    release_year=models.PositiveSmallIntegerField()
    rating=models.CharField(max_length=15)
