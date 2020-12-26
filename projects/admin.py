# Django
from django.contrib import admin
import admin_thumbnails

# local Django
from .models import Project


@admin.register(Project)
@admin_thumbnails.thumbnail("image")
class ProjectAdmin(admin.ModelAdmin):

    """ Project Admin Definition """

    list_display = (
        "title",
        "description",
        "image_thumbnail",
        "get_articles",
    )

    def get_articles(self, object):
        return object.article.count()

    get_articles.short_description = "number of articles"
