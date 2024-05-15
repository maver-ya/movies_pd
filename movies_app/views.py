from django.shortcuts import render, redirect

from movies_app.models import *
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import *

NAME = "RMDb"


# @login_required
def index(request):
    data = Movie.objects.order_by("-rating_kp")[:10]
    latest_movie1 = Movie.objects.order_by("-year")[:2]
    latest_movie2 = Movie.objects.order_by("-year")[2:6]
    comedies = Movie.objects.filter(genre__name="комедия").order_by("kinopoisk_id")[:5]
    dramas = Movie.objects.filter(genre__name="драма").order_by("kinopoisk_id")[:5]
    fighters = Movie.objects.filter(genre__name="боевик").order_by("kinopoisk_id")[:5]
    data = {"movies": data, "latest1": latest_movie1, "latest2": latest_movie2, "comedies": comedies, "dramas": dramas,
            "fighters": fighters, "title": NAME}
    return render(request, 'index.html', context=data)


def contact(request):
    data = {"title": NAME}
    return render(request, 'contact.html', context=data)


def about(request):
    data = {"title": NAME}
    return render(request, 'about.html', context=data)


def joinus(request):
    data = {"title": NAME}
    return render(request, 'joinus.html', context=data)


def review(request):
    genres = Genre.objects.all()
    country = Movie.objects.values("country__name")
    country = sorted(set(map(lambda x: x['country__name'], filter(lambda x: x['country__name'], country))))
    user_genre = request.GET.get("genre")
    user_country = request.GET.get("country")
    user_page = int(request.GET.get("page")) if request.GET.get("page") \
        else 0
    search = request.GET.get("search")
    print(user_page)
    ch_genres = [user_genre] if user_genre != "any" else list(map(lambda x: x, genres))
    ch_countries = [user_country] if user_country != "any" else list(map(lambda x: x, country))

    if search is None:
        movies = Movie.objects.filter(genre__name__in=ch_genres) & Movie.objects.filter(country__name__in=ch_countries)
    else:
        movies = Movie.objects.filter(genre__name__in=ch_genres) & Movie.objects.filter(country__name__in=ch_countries) & Movie.objects.filter(name__contains=search)

    movies = movies.distinct().order_by("kinopoisk_id")[user_page * 8:user_page * 8 + 8]
    if user_genre == "any": user_genre = "---"
    if user_country == "any": user_country = "---"
    data = {"genres": genres, "countries": country, 'user_genre': user_genre, "user_country": user_country,
            "movies": movies, 'title': NAME, "user_page": user_page}
    return render(request, 'review.html', context=data)


def single(request, id):
    movie = Movie.objects.filter(kinopoisk_id=id).first()
    reviews = Review.objects.filter(movie=movie).all()
    persons = movie.persons

    actors = persons.filter(profession__name="актеры")[:3]
    str_actors = ', '.join(list(map(lambda x: x.name, actors)))
    directors = persons.filter(profession__name="режиссеры")[:2]
    str_directors = ', '.join(list(map(lambda x: x.name, directors)))

    genres = movie.genre.all()[:4]
    str_genre = '/'.join(list(map(lambda x: x.name.capitalize(), genres)))

    data = {"reviews": reviews, "movie": movie, 'actors': str_actors, "directors": str_directors, "genres": str_genre,
            "title": NAME, "form": ReviewForm(initial={'movie': movie, 'user': User.objects.get()})}
    return render(request, 'single.html', context=data)


def submit_review(request):
    print(request.POST)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        print(form.get_context())
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            print("NO OK")
            form = ReviewForm()
            return render(request, '404.html')  # вывод ошибки


def profile_views(request):
    return render(request, 'profile.html')
