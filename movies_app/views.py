from django.shortcuts import render

from movies_app.models import *

NAME = "RMDb"


def index(request):
    data = Movie.objects.order_by("kinopoisk_id")[:10]
    latest_movie1 = Movie.objects.order_by("-year")[:2]
    latest_movie2 = Movie.objects.order_by("-year")[2:6]
    comedies = Movie.objects.filter(genre__name="комедия").order_by("kinopoisk_id")[:5]
    dramas = Movie.objects.filter(genre__name="драма").order_by("kinopoisk_id")[:5]
    fighters = Movie.objects.filter(genre__name="боевик").order_by("kinopoisk_id")[:5]
    data = {"movies": data, "latest1": latest_movie1, "latest2": latest_movie2, "comedies": comedies, "dramas": dramas,
            "fighters": fighters, "title": NAME}
    return render(request, 'index.html', context=data)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    data = {"title": NAME}
    return render(request, 'about.html', context=data)


def joinus(request):
    data = {"title": NAME}
    return render(request, 'joinus.html', context=data)


def review(request):
    genres = Genre.objects.all()
    country = Country.objects.all()

    user_genre = request.GET.get("genre")
    user_country = request.GET.get("country")
    user_page = int(request.GET.get("page"))
    print(user_page)
    ch_genres = [user_genre] if user_genre != "any" else list(map(lambda x: x.name, genres))
    ch_countries = [user_country] if user_country != "any" else list(map(lambda x: x.name, country))

    movies = Movie.objects.filter(genre__name__in=ch_genres) & Movie.objects.filter(country__name__in=ch_countries)

    movies = movies.distinct().order_by("kinopoisk_id")[user_page * 8:user_page * 8 + 8]
    if user_genre == "any": user_genre = "---"
    if user_country == "any": user_country = "---"
    data = {"genres": genres, "countries": country, 'user_genre': user_genre, "user_country": user_country,
            "movies": movies, 'title': NAME, "user_page": user_page}
    return render(request, 'review.html', context=data)


def single(request, id):
    movie = Movie.objects.filter(kinopoisk_id=id).first()

    persons = movie.persons

    actors = persons.filter(profession__name="актеры")[:3]
    str_actors = ', '.join(list(map(lambda x: x.name, actors)))
    directors = persons.filter(profession__name="режиссеры")[:2]
    str_directors = ', '.join(list(map(lambda x: x.name, directors)))

    genres = movie.genre.all()[:4]
    str_genre = '/'.join(list(map(lambda x: x.name.capitalize(), genres)))

    data = {"movie": movie, 'actors': str_actors, "directors": str_directors, "genres": str_genre, "title": NAME}
    return render(request, 'single.html', context=data)
