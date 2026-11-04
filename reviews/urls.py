from django.urls import path
from .views import AddReviewView, DeleteReviewView

urlpatterns = [
    path('places/<int:pk>/review/', AddReviewView.as_view(), name='add_review'),
    path('reviews/<int:pk>/delete/', DeleteReviewView.as_view(), name='delete_review'),
]