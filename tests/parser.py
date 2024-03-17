from requests import get

from tests.CONFIG import get_apikey
from tests.addDatabase import *


def fulfill_film_json(data):
    listFields = ['id', 'names', 'year', 'description',
                  'slogan', 'rating', 'ageRating', 'budget',
                  'movieLength', 'genres', 'countries', 'poster',
                  'persons', 'alternativeName']
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
                  'persons']
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
                new_person_profession = add_person_profession(new_person, profession)
                new_person_film = add_person_film(new_film, new_person)

                for g in data['genres']:
                    genre = Genre.objects.filter(name=g['name'])[0]
                    new_film_genre = add_film_genre(new_film, genre)

                for c in data['countries']:
                    country = Country.objects.filter(name=c['name'])[0]
                    new_film_country = add_film_country(new_film, country)


def main():
    movies = Movie.objects.all()
    used_ids = [movie.kinopoisk_id for movie in movies]
    all_ids = list(range(1306, 1000000))
    my_range = sorted(list(set(all_ids) - set(used_ids)))
    for i in my_range:
        main_parser(i)


def delete():
    Movie.objects.all().delete()
    Person.objects.all().delete()


if __name__ == "__main__":
    delete()