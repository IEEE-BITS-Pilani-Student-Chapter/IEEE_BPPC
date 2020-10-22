from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=80)
    # content = RichTextField(blank = True, null = True)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=40)
    img = models.ImageField(upload_to='post/', editable=True, blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog_view', kwargs={'pk': self.pk})

class Developers(models.Model):
    name = models.CharField(max_length = 30)
    post = models.CharField(max_length = 30)
    pic = models.ImageField(upload_to="developer/", editable=True, blank=True, default='person.png')
    bio = models.CharField(max_length = 250)
    git = models.URLField(max_length=130, unique=True, blank=True)
    linkein = models.URLField(max_length=130, unique=True, blank=True)

    def __str__(self):
        return self.name
