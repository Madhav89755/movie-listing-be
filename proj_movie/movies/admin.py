from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from .models import CollectionMovies, Genres
# Register your models here.


@admin.register(CollectionMovies)
class CollectionMovieAdmin(admin.ModelAdmin):

    @admin.action(description="Mark as favourite")
    def mark_favourite(self, request, queryset):
        queryset.update(is_favourite=True)
        self.message_user(
            request,
            ngettext(
                "%d collection was successfully marked as favourite.",
                "%d collections were successfully marked as favourite.",
                queryset.count(),
            )
            % queryset.count(),
            messages.SUCCESS,
        )

    @admin.action(description="Remove from favourite")
    def unmark_favourite(self, request, queryset):
        queryset.update(is_favourite=False)
        self.message_user(
            request,
            ngettext(
                "%d collection was successfully unmarked as favourite.",
                "%d collections were successfully unmarked as favourite.",
                queryset.count(),
            )
            % queryset.count(),
            messages.SUCCESS,
        )

    list_display = ["id",
                    "collection",
                    "movie_title",
                    "is_favourite",
                    "created_on",
                    "updated_on"]
    search_fields = ["id",
                     "movie_title",
                     "genres",
                     "is_favourite",
                     "collection__id",
                     "collection__collection_title"]
    list_filter = ["is_favourite"]
    actions = [mark_favourite, unmark_favourite]


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ["id",
                    "user",
                    "genre",
                    "movie_count",
                    "created_on",
                    "updated_on"]
    search_fields = ["id",
                     "user__id",
                     "user__email",
                     "user__username",
                     "genre"]
