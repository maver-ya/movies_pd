from django.shortcuts import render

from movies_app.models import *


def index(request):
    data = Movie.objects.order_by("kinopoisk_id")[:10]
    latest_movie1 = Movie.objects.order_by("-year")[:2]
    latest_movie2 = Movie.objects.order_by("-year")[2:6]
    comedies = Movie.objects.filter(genre__name="комедия").order_by("kinopoisk_id")[:5]
    dramas = Movie.objects.filter(genre__name="драма").order_by("kinopoisk_id")[:5]
    fighters = Movie.objects.filter(genre__name="боевик").order_by("kinopoisk_id")[:5]
    data = {"movies": data, "latest1": latest_movie1, "latest2": latest_movie2, "comedies": comedies, "dramas": dramas,
            "fighters": fighters}
    return render(request, 'index.html', context=data)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def joinus(request):
    return render(request, 'joinus.html')


def review(request):
    return render(request, 'review.html')


def single(request, id):
    movie = Movie.objects.filter(kinopoisk_id=id).first()

    persons = movie.persons

    actors = persons.filter(profession__name="актеры")[:3]
    str_actors = ', '.join(list(map(lambda x: x.name, actors)))
    directors = persons.filter(profession__name="режиссеры")[:2]
    str_directors = ', '.join(list(map(lambda x: x.name, directors)))

    genres = movie.genre.all()[:4]
    str_genre = '/'.join(list(map(lambda x: x.name.capitalize(), genres)))

    data = {"movie": movie, 'actors': str_actors, "directors": str_directors, "genres": str_genre}
    return render(request, 'single.html', context=data)
