from django.db import models
from django.contrib.auth.models import User
from places.models import Place


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(default=5)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.user.username} -> {self.place.title} ({self.rating}/5)"