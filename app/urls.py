from django.urls import include, path
from app.views import *

urlpatterns = [
    path('', home, name="home"),
    path('blogs/', blog_list, name='blogs'),
    path('blogs/detail', blog_view, name='blog_view'),
    path('developers/', dev_page, name='dev_page'),
]