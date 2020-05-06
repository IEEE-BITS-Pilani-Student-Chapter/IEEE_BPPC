from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def home(request):
    context = {}
    return render(request, 'app/home.html', context)

def dev_page(request):
    context = {}
    return render(request, 'app/dev.html', context);