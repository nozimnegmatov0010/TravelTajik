from django.db import models
from django.contrib.auth.models import User
from locations.models import City

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Place(models.Model):
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='added_places')
    city=models.ForeignKey(City,on_delete=models.CASCADE,related_name='places')
    categories=models.ManyToManyField(Category,related_name='places')
    title=models.CharField(max_length=255)
    description=models.TextField()
    address=models.CharField(max_length=255,blank=True)
    price_info=models.CharField(max_length=100,blank=True)
    image=models.ImageField(upload_to='places/',blank=True,null=True)
    map_url = models.URLField(max_length=500, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.city.name})"





