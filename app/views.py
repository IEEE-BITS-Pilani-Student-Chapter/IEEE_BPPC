from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Post


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'app/home.html', context)

def dev_page(request):
    context = {}
    return render(request, 'app/dev.html', context);

def blog_list(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'app/blog_list.html', context)

def blog_view(request):
    context = {}
    return render(request, 'app/blog_view.html', context)