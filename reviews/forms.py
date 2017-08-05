from django.forms import ModelForm, Textarea
from .models import Review,Wine


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }


class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = ['name']
