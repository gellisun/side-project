from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup', views.signup, name='signup'),
    path('galleries/', views.galleries_index, name='galleries_index'),
    path('galleries/<int:gallery_id>/', views.galleries_detail, name='galleries_detail'),
    path('galleries/<int:gallery_id>/exhibition/create', views.exhibition_create, name='exhibition_create'),
    path('api/save-exhibition/<int:exhibition_id>/', views.save_exhibition, name='save_exhibition'),
    path('exhibitions/saved/', views.exhibitions_saved, name='exhibitions_saved'),
    path('api/delete-exhibition/<int:exhibition_id>/', views.delete_exhibition, name='delete_exhibition'),
]
