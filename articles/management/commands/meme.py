# Python
import requests
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

# Django
from django.core.files import File
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth.management.commands import createsuperuser

# local Django
from articles.models import Article


class Command(createsuperuser.Command):
    help = "This Command creates meme articles"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many meme article you want to create"
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        for _ in range(number):
            meme = requests.get("https://meme-api.herokuapp.com/gimme").json()
            title = meme.get("title")
            url = meme.get("url")
            postlink = meme.get("postLink")
            postlink = mark_safe(f"<a href='{postlink}'>출처</a>")
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(url).read())
            img_temp.flush()

            article = Article.objects.create(
                title=title,
                content=postlink,
                writer=User.objects.get(username="wjddnr3315@naver.com"),
            )
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(url).read())
            img_temp.flush()

            article.image.save("image_%s" % article.pk, File(img_temp))
            article.save()
