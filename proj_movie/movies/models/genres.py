import uuid
from django.db import models
from django.contrib.auth.models import User
from utils.abstract.models import DateTime
# Create your models here.


class Genres(DateTime):
    id=models.UUIDField("ID",
                        default=uuid.uuid4,
                        primary_key=True,
                        editable=False)
    user=models.ForeignKey(User,
                           verbose_name="User",
                           on_delete=models.CASCADE,
                           related_name="movies_genres")
    genre = models.CharField("Genres Title", max_length=256)
    movie_count=models.BigIntegerField("Movie Count", default=0)

    def __str__(self) -> str:
        return f"{self.user.id} - {self.genre}"

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering=["-created_on"]
