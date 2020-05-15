from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=40)

class Developers(models.Model):
    Name = models.CharFeilds(max_length = 30)
    Post = models.CharFeilds(max_length = 30)
    Pic = models.ImageField(upload_to="gallery")
    img src="/media/person.png"
    Bio = models.CharFeilds(max_Length = 200)
    class Social_links(models.Model):
        Github = models.URLFeild(_("git"),max_length=128,db_index = True, unique=True, blank=True)
        LinkedIn = models.URLFeild(_("LinkedIn"),max_length=128,db_index = True, unique=True, blank=True)

    def __str__(self):
        return self.title
