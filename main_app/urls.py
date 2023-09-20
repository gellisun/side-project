from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('galleries/', views.galleries_index, name='galleries_index'),
    path('galleries/<int:gallery_id>/', views.galleries_detail, name='galleries_detail'),
    path('galleries/<int:gallery_id>/exhibition/create', views.exhibition_create, name='exhibition_create'),
]
