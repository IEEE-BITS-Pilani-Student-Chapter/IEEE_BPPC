from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Post


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'app/home.html', context)
