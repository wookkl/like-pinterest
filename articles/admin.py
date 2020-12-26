# Django
from django.contrib import admin
import admin_thumbnails

# local Django
from .models import Article


@admin.register(Article)
@admin_thumbnails.thumbnail("image")
class ArticleAdmin(admin.ModelAdmin):

    """ Article Admin Definition """

    list_display = (
        "writer",
        "project",
        "title",
        "image_thumbnail",
    )
