from . import views
from django.urls.conf import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.utils import translation



urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()