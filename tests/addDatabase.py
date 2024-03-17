from movies_app.models import *


def add_person(data):
    name = data['name']
    if name is None:
        return 0
    photo = data['photo']
    persons = Person.objects.filter(name=name, photo=photo).exists()
    if not persons:
        new_person = Person(name=name, photo=photo)
        new_person.save()
        return new_person
    return Person.objects.filter(name=name, photo=photo)[0]


def add_person_profession(person, profession):
    db_data = PersonProfession.objects.filter(person_id=person, profession_id=profession).exists()
    if not db_data:
        new_person_profession = PersonProfession(person_id=person, profession_id=profession)
        new_person_profession.save()


def add_film(data):
    film_existing = Movie.objects.filter(kinopoisk_id=data['id']).exists()
    if not film_existing:
        new_film = Movie(
            name=data['name'],
            year=data['year'],
            description=data['description'],
            duration=data['movieLength'],
            budget=data['budget'],
            rate=data['ageRating'],
            kinopoisk_id=data['id'],
            rating_kp=data['rating']['kp'],
            rating_imdb=data['rating']['imdb'],
            poster=data['poster']['url']
        )
        try:
            new_film.save()
            print(data['name'])
            return new_film
        except Exception as e:
            print(e)
            print(f"film_id: {data['id']}")


def add_person_film(film, person):
    if not MoviePerson.objects.filter(movie=film, person=person).exists():
        new = MoviePerson(movie=film, person=person)
        new.save()


def add_film_genre(film, genre):
    if not MovieGenre.objects.filter(movie_id=film, genre_id=genre).exists():
        new = MovieGenre(movie_id=film, genre_id=genre)
        new.save()


def add_film_country(film, country):
    if not MovieCountry.objects.filter(movie_id=film, country_id=country).exists():
        new = MovieCountry(movie_id=film, country_id=country)
        new.save()