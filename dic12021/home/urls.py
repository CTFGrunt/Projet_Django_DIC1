from . import views
from django.urls.conf import path



urlpatterns = [
    path('contact/',views.contact,name="contact"),
    path('',views.index, name="index"),
]
