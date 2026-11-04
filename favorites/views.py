from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from places.models import Place
from .models import Favorite


class ToggleFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        place = get_object_or_404(Place, pk=pk)
        favorite, created = Favorite.objects.get_or_create(user=request.user, place=place)
        if not created:
            favorite.delete()  
        return redirect(request.META.get('HTTP_REFERER', reverse_lazy('place_list')))


class FavoriteListView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = 'favorites/favorite_list.html'
    context_object_name = 'favorites'

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).select_related(
            'place', 'place__city', 'place__city__region'
        )
