from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('add/',views.add,name ='add'),
    path('add/addrecord/',views.addrecord,name="addrecord"),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('delete/<int:id>',views.delete,name='delete')
]
