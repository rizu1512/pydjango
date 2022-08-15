


from django.urls import path,include
from . import views
urlpatterns = [
   
    path('',views.main,name="main"),
    path('add/',views.add,name='add'),
    path('form/', views.my_form, name='form')
    
]
