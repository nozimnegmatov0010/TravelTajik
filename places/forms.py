from django import forms
from .models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title', 'city', 'categories', 'description', 'address', 'price_info', 'image', 'map_url']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-xl border border-stone-300 focus:outline-none focus:ring-2 focus:ring-[#1B6B4F]',
                'placeholder': 'Например: Озеро Искандеркуль'
            }),
            'city': forms.Select(attrs={
                'class': 'w-full p-3 rounded-xl border border-stone-300 bg-white focus:outline-none focus:ring-2 focus:ring-[#1B6B4F]'
            }),
            'categories': forms.CheckboxSelectMultiple(attrs={
                'class': 'rounded text-[#1B6B4F] focus:ring-[#1B6B4F]'
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'class': 'w-full p-3 rounded-xl border border-stone-300 focus:outline-none focus:ring-2 focus:ring-[#1B6B4F]',
                'placeholder': 'Расскажите об истории, природе и особенностях этого места...'
            }),
            'address': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-xl border border-stone-300 focus:outline-none focus:ring-2 focus:ring-[#1B6B4F]',
                'placeholder': 'Например: проспект Рудаки, 33 или 130 км от Душанбе'
            }),
            'price_info': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-xl border border-stone-300 focus:outline-none focus:ring-2 focus:ring-[#1B6B4F]',
                'placeholder': 'Например: Вход 20 сомони / Гостевые дома 15-25$'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2.5 rounded-xl border border-stone-300 bg-white'
            }),
            'map_url': forms.URLInput(attrs={
                'class': 'w-full p-3 rounded-xl border border-stone-300 focus:outline-none focus:ring-2 focus:ring-[#1B6B4F]',
                'placeholder': 'Вставьте ссылку на Google Maps, Яндекс.Карты или 2ГИС (https://...)'
            }),
        }