from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from places.models import Place
from .models import Review


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, pk):
        place = get_object_or_404(Place, pk=pk)
        rating = request.POST.get('rating')
        text = request.POST.get('text')

        if rating and text:
            Review.objects.create(
                user=request.user,
                place=place,
                rating=int(rating),
                text=text
            )
        return redirect('place_detail', pk=pk)


class DeleteReviewView(LoginRequiredMixin, View):
    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        place_pk = review.place.pk

        if request.user == review.user or request.user.is_staff:
            review.delete()

        return redirect('place_detail', pk=place_pk)