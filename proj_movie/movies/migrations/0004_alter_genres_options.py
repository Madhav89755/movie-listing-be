# Generated by Django 5.1 on 2024-08-09 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_alter_genres_options_alter_genres_movie_count"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="genres",
            options={
                "ordering": ["-movie_count", "-created_on"],
                "verbose_name": "Genre",
                "verbose_name_plural": "Genres",
            },
        ),
    ]