# Generated by Django 5.1 on 2024-08-09 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("collection", "0001_initial"),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="collectionmovies",
            unique_together={("uuid_col", "collection")},
        ),
    ]
