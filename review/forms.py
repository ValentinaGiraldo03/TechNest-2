from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment', 'rating')
        widgets = {
            'rating': forms.NumberInput(attrs={'min': '1', 'max': '5'}),
        }
        error_messages = {
            'rating': {
                'min_value': 'The rating must be at least 1 star.',
                'max_value': 'The rating cannot be more than 5 stars.',
            }
        }

        