from unicodedata import name
from django.urls import path
from c9 import views
urlpatterns = [
    path('',views.index),
    path('contact/',views.contact ,name='contact')
]