# Django
from django.contrib import admin
from django.contrib.auth.models import User


class UserAdmin(admin.ModelAdmin):

    """ User Admin Definition """

    list_display = (
        "username",
        "email",
        "subscriptions",
    )

    def subscriptions(self, object):
        return object.subscriptions.count()

    subscriptions.short_description = "number of subscriptions"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
