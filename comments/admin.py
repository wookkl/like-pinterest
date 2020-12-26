# Django
from django.contrib import admin

# local Django
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    """ Comment Admin Definition """

    list_display = (
        "article",
        "writer",
        "content",
    )
