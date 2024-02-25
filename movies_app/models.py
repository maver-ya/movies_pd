from django.db import models

from .base import TimeStampedModel


class Movie(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    description = models.TextField()
    duration = models.PositiveIntegerField()
    budget = models.CharField(max_length=255)
    rate = models.PositiveIntegerField()
    kinopoisk_id = models.PositiveIntegerField()
    rating_kp = models.PositiveIntegerField()
    rating_imdb = models.PositiveIntegerField()
    poster = models.CharField(max_length=255)

    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.name


class Person(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    country_id = models.ForeignKey('movies_app.Country', on_delete=models.CASCADE, related_name="nation")
    sex = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)

    class Meta:
        db_table = 'persons'

    def __str__(self):
        return self.name


class Profession(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'profession'

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


class MoviePerson(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    movie = models.ForeignKey('movies_app.Movie', on_delete=models.CASCADE, related_name='people')
    person = models.ForeignKey('movies_app.Person', on_delete=models.CASCADE, related_name='roles')

    class Meta:
        db_table = 'moviePerson'

    def __str__(self):
        return f'{self.id} ({self.movie}, {self.person})'


class PersonProfession(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    person_id = models.ForeignKey('movies_app.Person', on_delete=models.CASCADE, related_name='professions')
    profession_id = models.ForeignKey('movies_app.Profession', on_delete=models.CASCADE, related_name='performers')

    class Meta:
        db_table = 'personProfession'

    def __str__(self):
        return f'{self.id} ({self.person_id}, {self.profession_id})'


class MovieGenre(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    movie_id = models.ForeignKey('movies_app.Movie', on_delete=models.CASCADE, related_name="mg")
    genre_id = models.ForeignKey('movies_app.Genre', on_delete=models.CASCADE, related_name="gm")

    class Meta:
        db_table = 'movieGenre'


class MovieCountry(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    movie_id = models.ForeignKey('movies_app.Movie', on_delete=models.CASCADE, related_name="mc")
    country_id = models.ForeignKey('movies_app.Country', on_delete=models.CASCADE, related_name="cm")

    class Meta:
        db_table = 'movieCountry'
