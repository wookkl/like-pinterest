# Django
from django.db import models
from django.contrib.auth.admin import User


class Account(User):

    """ Account Model Definition """

    LOGIN_GITHUB = "GH"
    LOGIN_KAKAO = "KK"
    LOGIN_EMAIL = "EM"
    CHOICES_LOGIN = (
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
        (LOGIN_EMAIL, "Email"),
    )

    login_method = models.CharField(
        max_length=2, choices=CHOICES_LOGIN, default=LOGIN_EMAIL
    )
