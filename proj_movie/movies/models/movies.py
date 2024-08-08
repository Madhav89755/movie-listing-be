import uuid
from django.db import models
from utils.abstract.models import DateTime
# Create your models here.


class CollectionMovies(DateTime):
    id = models.UUIDField("uuid",
                          default=uuid.uuid4,
                          primary_key=True)
    collection = models.ForeignKey("collection.Collection",
                                   verbose_name="Collection",
                                   related_name="collection_movies",
                                   on_delete=models.CASCADE)
    movie_title = models.CharField("Movie Title", max_length=256)
    description = models.TextField("Description")
    genres = models.CharField("Genres", max_length=256)
    is_favourite=models.BooleanField("Is Favourite", default=False)

    def __str__(self) -> str:
        return self.movie_title.title()

    class Meta:
        verbose_name = "Collection Movie"
        verbose_name_plural = "Collection Movies"
        ordering = ["-created_on"]
