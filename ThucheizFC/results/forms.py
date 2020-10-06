from django import forms
import datetime

from main.models import Player
from results.models import Result, ClubGoal, OpponentGoal


class ResultCreationForm(forms.ModelForm):
    club_goal = forms.ModelMultipleChoiceField(queryset=ClubGoal.objects.all(),
                                               widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})),
    opponent_goal = forms.ModelMultipleChoiceField(queryset=OpponentGoal.objects.all(),
                                                   widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date > datetime.date.today():
            raise forms.ValidationError('Match date should not be greater than today !!!!')
        return date

    class Meta:
        model = Result
        fields = ['result_type', 'club_goal', 'opponent', 'image', 'opponent_goal', 'stadium', 'date']
        widgets = {
            'result_type': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stadium': forms.TextInput(attrs={'class': 'form-control'})
        }


class ClubGoalCreationForm(forms.ModelForm):
    player = forms.ModelChoiceField(queryset=Player.objects.filter(available=True),
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ClubGoal
        fields = ['player', 'minute']
        widgets = {

            'minute': forms.NumberInput(attrs={'class': 'form-control'})
        }


class OpponentGoalCreationForm(forms.ModelForm):
    class Meta:
        model = OpponentGoal
        fields = ['scorer', 'minute']
        widgets = {
            'scorer': forms.TextInput(attrs={'class': 'form-control'}),
            'minute': forms.NumberInput(attrs={'class': 'form-control'})
        }