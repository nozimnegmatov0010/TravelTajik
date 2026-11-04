from django.db import models

from django.contrib.auth.models import User
from places.models import Place


class Favorite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='favorites')
    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

   

    def __str__(self):
        return f"{self.user.username} -> {self.place.title}"
