# Generated by Django 5.1 on 2024-08-09 12:09

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Collection",
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
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "collection_title",
                    models.CharField(max_length=256, verbose_name="Collection Title"),
                ),
                (
                    "description",
                    models.TextField(null=True, verbose_name="Description"),
                ),
                (
                    "is_favourite",
                    models.BooleanField(default=False, verbose_name="Is Favourite"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="collections_created",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Collection",
                "verbose_name_plural": "Collection",
                "ordering": ["-created_on"],
            },
        ),
    ]
