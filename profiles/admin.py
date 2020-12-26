# Django
from django.contrib import admin
import admin_thumbnails

# local Django
from .models import Profile


@admin.register(Profile)
@admin_thumbnails.thumbnail("image")
class ProfileAdmin(admin.ModelAdmin):

    """ Profile Admin Definition """

    list_display = (
        "user",
        "image_thumbnail",
        "nickname",
        "status_message",
    )
