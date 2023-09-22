from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User
class Gallery(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=800)
    hours = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('gallery_detail', kwargs={'gallery_id': self.id})
    
class Exhibition(models.Model):
    name = models.CharField(max_length=150)
    closingDate = models.DateField()
    description = models.TextField(max_length=600)
    feedback = models.TextField(max_length=600)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.name