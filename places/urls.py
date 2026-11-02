from django.urls import path
from .views import (PlaceListView,PlaceDetailView,PlaceCreateView,PlaceUpdateView,PlaceDeleteView)

urlpatterns = [
    path('', PlaceListView.as_view(), name='place_list'),
    path('places/', PlaceListView.as_view(), name='place_catalog'),
    path('places/create/', PlaceCreateView.as_view(), name='place_create'),
    path('places/<int:pk>/', PlaceDetailView.as_view(), name='place_detail'),
    path('places/<int:pk>/edit/', PlaceUpdateView.as_view(), name='place_edit'),
    path('places/<int:pk>/delete/', PlaceDeleteView.as_view(), name='place_delete'),
]