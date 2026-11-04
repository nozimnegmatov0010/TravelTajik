from django.urls import path
from .views import ToggleFavoriteView, FavoriteListView

urlpatterns = [
    path('favorites/', FavoriteListView.as_view(), name='favorite_list'),
    path('places/<int:pk>/favorite/', ToggleFavoriteView.as_view(), name='toggle_favorite'),
]