# Generated by Django 5.1 on 2024-08-08 18:11

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("collection", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CollectionMovies",
            fields=[
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created On"),
                ),
                (
                    "updated_on",
                    models.DateTimeField(auto_now=True, verbose_name="Updated On"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="uuid",
                    ),
                ),
                (
                    "movie_title",
                    models.CharField(max_length=256, verbose_name="Movie Title"),
                ),
                ("description", models.TextField(verbose_name="Description")),
                ("genres", models.CharField(max_length=256, verbose_name="Genres")),
                ("is_favourite", models.BooleanField(verbose_name="Is Favourite")),
                (
                    "collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="collection_movies",
                        to="collection.collection",
                        verbose_name="Collection",
                    ),
                ),
            ],
            options={
                "verbose_name": "Collection Movie",
                "verbose_name_plural": "Collection Movies",
                "ordering": ["-created_on"],
            },
        ),
        migrations.CreateModel(
            name="Genres",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created On"),
                ),
                (
                    "updated_on",
                    models.DateTimeField(auto_now=True, verbose_name="Updated On"),
                ),
                (
                    "genre",
                    models.CharField(max_length=256, verbose_name="Genres Title"),
                ),
                (
                    "movie_count",
                    models.BigIntegerField(default=0, verbose_name="Movie Count"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movies_genres",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Genre",
                "verbose_name_plural": "Genres",
                "ordering": ["-created_on"],
            },
        ),
    ]
