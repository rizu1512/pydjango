from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.project_index,name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),

]
