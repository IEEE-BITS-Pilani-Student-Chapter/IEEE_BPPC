from django.urls import include, path
from app.views import *

urlpatterns = [
    path('', home),
]