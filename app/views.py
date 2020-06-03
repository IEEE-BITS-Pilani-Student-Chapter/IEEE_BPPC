from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Post, Developers
from .forms import PostForm

import random

def home(request):
    posts = Post.objects.all()
    cnt = int(posts.count()/3);
    if cnt>6:
        cnt = 6
    posts = posts[0:cnt]
    context = {'posts': posts}
    return render(request, 'app/home.html', context)


def dev_page(request):
    context = {}
    return render(request, 'app/dev.html', context);


def blog_list(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'app/blog_list.html', context)

def blog_view(request, pk):
    context = {}
    try:
        context['post'] = Post.objects.get(pk=pk)
        context['extra'] = Post.objects.all()[0:3] # top 3 artices for recommendations
    except:
        return redirect(home)
    return render(request, 'app/blog_view.html', context)

def post_image_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PostForm()
    return render(request, 'app/post_form.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')
