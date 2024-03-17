from requests import get

from tests.CONFIG import get_apikey
from tests.addDatabase import *


def fulfill_film_json(data):
    listFields = ['id', 'names', 'year', 'description',
                  'slogan', 'rating', 'ageRating', 'budget',
                  'movieLength', 'genres', 'countries', 'poster',
                  'persons', 'alternativeName', 'type']
    for key in listFields:
        if key not in data.keys():
            if key in ['year', 'duration', 'ageRating']:
                data[key] = 1000
            elif key in ['rating']:
                data[key] = {}
                data[key]['kp'] = -1
                data[key]['imdb'] = -1
            else:
                if key == 'poster':
                    data[key] = {"url": ""}
                else:
                    data[key] = ""
        if key == 'ageRating' and data[key] == 'null':
            data[key] = 100
        if key == 'budget' and data[key]:
            data[key] = f"{data[key]['value']} {data[key]['currency']}"
        if data['ageRating'] is None:
            data['ageRating'] = 100
    return data


def parser_film(film_id):
    if Movie.objects.filter(kinopoisk_id=film_id).exists():
        return 0
    url = "https://api.kinopoisk.dev/v1.4/movie"
    listFields = ['id', 'name', 'year', 'description',
                  'slogan', 'rating', 'ageRating', 'budget',
                  'movieLength', 'genres', 'countries', 'poster',
                  'persons', 'type']
    response = get(url, headers={"X-API-KEY": get_apikey()},
                   params={"id": film_id, 'selectFields': listFields})
    data = response.json()
    try:
        data = fulfill_film_json(data['docs'][0])
        return data
    except Exception as e:
        print(e)
        print(data)
        return 0


def parser_person(person_id):
    url_person = "https://api.kinopoisk.dev/v1.4/person"
    data = get(url=url_person, headers={"X-API-KEY": get_apikey()},
               params={"id": person_id,
                       "listFields": ['name', 'id', 'photo']}).json()
    data = data['docs'][0]
    name = data['name']
    photo = data.get("photo", "")
    return {"name": name, "photo": photo}


def main_parser(film_id):
    data = parser_film(film_id)
    if not data:
        return 0

    # add film
    new_film = add_film(data)
    if new_film:
        # add persons
        persons = data['persons']
        for person in persons:
            prof = person['profession']
            if prof in ['актеры', 'режиссеры']:
                profession = Profession.objects.filter(name=prof)[0]
                new_person = add_person(person)
                if not new_person:
                    continue
                new_person.profession.add(profession)
                new_person.save()
                new_film.persons.add(new_person)
                new_film.save()
                for g in data['genres']:
                    genre = Genre.objects.filter(name=g['name'])[0]
                    new_film.genre.add(genre)
                for c in data['countries']:
                    country = Country.objects.filter(name=c['name'])[0]
                    new_film.country.add(country)


def main():
    movies = Movie.objects.all()
    used_ids = [movie.kinopoisk_id for movie in movies]
    all_ids = list(range(max(used_ids), 1000000))
    for i in all_ids:
        main_parser(i)


def get_film_by_actor():
    persons = Person.objects.all()
    for person in persons:
        movies = Movie.objects.filter(persons__name=person.name)
        names = list(map(lambda x: x.name, movies))
        print(person.name)
        print(*names, sep='\n')
        print()


if __name__ == "__main__":
    main()
