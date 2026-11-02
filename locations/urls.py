from django.urls import path
from .views import RegionListView, RegionDetailView, CityDetailView

urlpatterns = [
    path('regions/', RegionListView.as_view(), name='region_list'),
    path('regions/<int:pk>/', RegionDetailView.as_view(), name='region_detail'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='city_detail'),
]