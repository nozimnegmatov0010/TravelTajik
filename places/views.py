from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q, Avg
from locations.models import Region, City
from .models import Place, Category
from .forms import PlaceForm


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class PlaceListView(ListView):
    model = Place
    template_name = 'places/place_list.html'
    context_object_name = 'places'
    paginate_by = 9

    def get_queryset(self):
        queryset = Place.objects.select_related('city', 'city__region', 'author').prefetch_related('categories').annotate(
            avg_rating=Avg('reviews__rating')
        )

        q = self.request.GET.get('q')
        region_id = self.request.GET.get('region')
        city_id = self.request.GET.get('city')
        category_id = self.request.GET.get('category')

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q) |
                Q(city__name__icontains=q)
            )
        if region_id:
            queryset = queryset.filter(city__region_id=region_id)
        if city_id:
            queryset = queryset.filter(city_id=city_id)
        if category_id:
            queryset = queryset.filter(categories__id=category_id)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.all()
        context['cities'] = City.objects.select_related('region').all()
        context['categories'] = Category.objects.all()
        return context


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'places/place_detail.html'
    context_object_name = 'place'

    def get_queryset(self):
        return Place.objects.select_related('city', 'city__region', 'author').prefetch_related(
            'categories', 'reviews__user'
        ).annotate(avg_rating=Avg('reviews__rating'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['is_favorited'] = self.object.favorited_by.filter(user=self.request.user).exists()
        return context


class PlaceCreateView(AdminRequiredMixin, CreateView):
    model = Place
    form_class = PlaceForm
    template_name = 'places/place_form.html'
    success_url = reverse_lazy('place_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PlaceUpdateView(AdminRequiredMixin, UpdateView):
    model = Place
    form_class = PlaceForm
    template_name = 'places/place_form.html'

    def get_success_url(self):
        return reverse_lazy('place_detail', kwargs={'pk': self.object.pk})


class PlaceDeleteView(AdminRequiredMixin, DeleteView):
    model = Place
    template_name = 'places/place_confirm_delete.html'
    success_url = reverse_lazy('place_list')