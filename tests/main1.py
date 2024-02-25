def zaebis():
    from requests import get
    from movies_app.models import Person, Movie, Genre, Profession, MovieGenre, MoviePerson, MovieCountry, PersonProfession, Country

    api_key = "YCZD8N5-YDB48VH-G6S7GBP-B3BSPE8"
    url = "https://api.kinopoisk.dev/v1.4/movie"
    response = get(url, headers={"X-API-KEY": api_key}, params={"lists": "top250", "limit": 250})

    data = response.json()['docs']

    db_data = []
    for line in data:
        d = {
            "name": line["names"][0]['name'],
            "year": line['year'],
            "description": line['description'],
            "slogan": line.get("slogan", None),
            "duration": line['movieLength'],
            "rate": line['ageRating'],
            "kinopoisk_id": line['id'],
            "rating_kp": line['rating']['kp'],
            "rating_imdb": line['rating']['imdb'],
            "poster": line['poster']['url']
        }
        db_data.append(d)

    url_for_film = "https://api.kinopoisk.dev/v1.4/movie"
    for film in db_data:
        film_id = film['kinopoisk_id']
        response = get(url, headers={"X-API-KEY": api_key}, params={"id": film_id, "limit": 1,
                                                                    "selectFields": ["countries", "persons", "id", "genres",
                                                                                     "budget"]})

        data = response.json()
        data = data['docs'][0]

        genres = data['genres']
        genres = list(map(lambda x: x['name'], genres))

        budget = data['budget']
        if not budget:
            budget = None
        else:
            budget = f"{budget['value']}{budget['currency']}"

        new_movie = Movie(
            name=film["name"],
            year=film['year'],
            description=film['description'],
            duration=film['duration'],
            budget=budget,
            rate=film['rate'],
            kinopoisk_id=film['kinopoisk_id'],
            rating_kp=film['rating_kp'],
            rating_imdb=film['rating_imdb'],
            poster=film['poster']
        )
        movie = new_movie.save()
        movie_id = movie.id

        for g in genres:
            genre_id = Genre.objects.filter(name=g).id
            new_movie_genre = MovieGenre(
                movie_id=movie_id,
                genre_id=genre_id
            )
            new_movie_genre.save()
        country = data['countries']
        country = list(map(lambda x: x['name'], country))
        for c in country:
            country_id = Country.objects.filter(name=c).id
            new_country_movie = MovieCountry(
                movie_id=movie.id,
                country_id=country_id
            )
            new_country_movie.save()

        persons = data['persons']

        for p in persons:
            prof = p['profession']
            if prof in ["режиссеры", "актеры"]:
                name = p['name']
                photo = p['photo']
                person_id = p['id']
            else:
                continue
            url_person = "https://api.kinopoisk.dev/v1.4/person"
            p_data = get(url=url_person, headers={"X-API-KEY": api_key}, params={"id": person_id}).json()
            country = p_data['birthPlace'][1]['value']
            sex = p_data['sex']
            year = p_data['birthday'].split('-')[0]
            country_id = Country.objects.filter(name=country).id

            new_person = Person(
                name=name,
                year=int(year),
                country_id=country_id,
                sex=sex,
                photo=photo
            )
            pers = new_person.save()

            person_id = pers.id
            prof_id = Profession.objects.filter(name=prof).id
            new_person_profession = PersonProfession(
                person_id=person_id,
                profession_id=profession_id
            )
            new_person_profession.save()

            new_person_movie = MoviePerson(
                movie=movie_id,
                person=person_id
            )
