from django.contrib import admin

from .models import *

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Profession)
admin.site.register(Rating)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(MoviePerson)
admin.site.register(PersonProfession)
admin.site.register(MovieGenre)
admin.site.register(MovieCountry)