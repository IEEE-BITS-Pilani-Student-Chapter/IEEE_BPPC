from django.urls import include, path
from app.views import *

urlpatterns = [
    path('', home, name="home"),
    path('developers/', dev_page, name='dev_page'),
]