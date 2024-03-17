from django.db import models

from .base import TimeStampedModel


class Profession(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'profession'

    def __str__(self):
        return self.name


class Person(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, default="")
    profession = models.ManyToManyField(Profession)

    class Meta:
        db_table = 'persons'

    def __str__(self):
        return self.name


class Rating(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    movie_id = models.ForeignKey('movies_app.Movie', on_delete=models.CASCADE, related_name="films")
    user_rate = models.PositiveIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        db_table = 'rating'

    def __str__(self):
        return str(self.movie_id) + '-' + str(self.user_id)


class Country(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'countries'

    def __str__(self):
        return self.name


class Genre(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.name


class Movie(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    description = models.TextField()
    duration = models.PositiveIntegerField()
    budget = models.CharField(max_length=255)
    rate = models.PositiveIntegerField()
    kinopoisk_id = models.PositiveIntegerField()
    rating_kp = models.FloatField()
    rating_imdb = models.FloatField()
    poster = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    country = models.ManyToManyField(Country)
    persons = models.ManyToManyField(Person)
    movie_type = models.CharField(max_length=20)

    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.name
