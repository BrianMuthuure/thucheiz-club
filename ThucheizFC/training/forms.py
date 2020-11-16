from django import forms

from training.models import TrainingSession


class TrainingForm(forms.ModelForm):

    class Meta:

        model =TrainingSession
        fields = ('date', 'player', 'coach', 'status', 'active')

        widgets = {
             'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'select date', 'type': 'date'})
        }
