# Generated by Django 5.0.2 on 2024-02-24 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('slogan', models.CharField(max_length=255)),
                ('duration', models.PositiveIntegerField()),
                ('budget', models.PositiveIntegerField()),
                ('rate', models.PositiveIntegerField()),
                ('kinopoisk_id', models.PositiveIntegerField()),
                ('rating_kp', models.PositiveIntegerField()),
                ('rating_imdb', models.PositiveIntegerField()),
                ('poster', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'profession',
            },
        ),
        migrations.CreateModel(
            name='MovieCountry',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cm', to='movies_app.country')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mc', to='movies_app.movie')),
            ],
            options={
                'db_table': 'movieCountry',
            },
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gm', to='movies_app.genre')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mg', to='movies_app.movie')),
            ],
            options={
                'db_table': 'movieGenre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField()),
                ('sex', models.CharField(max_length=255)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nation', to='movies_app.country')),
            ],
            options={
                'db_table': 'persons',
            },
        ),
        migrations.CreateModel(
            name='MoviePerson',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people', to='movies_app.movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='movies_app.person')),
            ],
            options={
                'db_table': 'moviePerson',
            },
        ),
        migrations.CreateModel(
            name='PersonProfession',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professions', to='movies_app.person')),
                ('profession_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performers', to='movies_app.profession')),
            ],
            options={
                'db_table': 'personProfession',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_rate', models.PositiveIntegerField()),
                ('user_id', models.BigIntegerField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='films', to='movies_app.movie')),
            ],
            options={
                'db_table': 'rating',
            },
        ),
    ]
