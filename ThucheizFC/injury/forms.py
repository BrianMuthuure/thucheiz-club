from django import forms

from injury.models import Injury
from main.models import Player


class InjuryForm(forms.ModelForm):
    injury_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    player = forms.ModelChoiceField(queryset=Player.objects.available(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Injury
        fields = ['injury_type', 'player']

