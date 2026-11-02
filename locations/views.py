from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.db.models import Count
from .models import Region, City


class RegionListView(ListView):
    model = Region
    template_name = 'locations/region_list.html'
    context_object_name = 'regions'

    def get_queryset(self):
        return Region.objects.annotate(
            cities_count=Count('cities')
        ).prefetch_related('cities')


class RegionDetailView(DetailView):
    model = Region
    template_name = 'locations/region_detail.html'
    context_object_name = 'region'

    def get_queryset(self):
        return Region.objects.prefetch_related('cities')


class CityDetailView(DetailView):
    model = City
    template_name = 'locations/city_detail.html'
    context_object_name = 'city'

    def get_queryset(self):
        return City.objects.select_related('region')