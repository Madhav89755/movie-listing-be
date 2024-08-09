import uuid
from django.db import models
from django.contrib.auth.models import User
from utils.abstract.models import DateTime
from movies.models import Genres
# Create your models here.


class Collection(DateTime):
    id=models.UUIDField("ID",
                        default=uuid.uuid4,
                        primary_key=True,
                        editable=False)
    user = models.ForeignKey(User,
                             verbose_name="User",
                             on_delete=models.CASCADE,
                             related_name="collections_created")
    collection_title = models.CharField("Collection Title", max_length=256)
    description = models.TextField("Description", null=True)
    is_favourite=models.BooleanField("Is Favourite", default=False)

    def __str__(self) -> str:
        return self.collection_title.title()
    
    def delete(self):
        movie_objs=self.collection_movies.all()
        if movie_objs.count()>0:
            genres_obj=Genres.objects.filter(user=self.user)
            for movie in movie_objs:
                genres=movie.get_genres
                for x in genres:
                    genres_obj.get(genre=x).decrease_count
            movie_objs.delete()
        return super(Collection, self).delete()

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collection"
        ordering = ["-created_on"]
        unique_together=("user", "collection_title")
