from app.views import *
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('', home, name="home"),
    path('blogs/', blog_list, name='blogs'),
    path('blogs/detail', blog_view, name='blog_view'),
    path('developers/', dev_page, name='dev_page'),
    path('image_upload', post_image_view, name='image_upload'),
    path('success', success, name='success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
