from django import forms
import datetime

from main.models import Player
from results.models import Result, GoalsScored, GoalsConceded


class ResultCreationForm(forms.ModelForm):

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date > datetime.date.today():
            raise forms.ValidationError('Match date should not be greater than today !!!!')
        return date

    class Meta:
        model = Result
        fields = ['result_type', 'opponent', 'image', 'stadium', 'date']
        widgets = {
            'result_type': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stadium': forms.TextInput(attrs={'class': 'form-control'})
        }


class ClubGoalForm(forms.ModelForm):
    player = forms.ModelChoiceField(queryset=Player.objects.all(), widget=forms.Select())

    class Meta:
        model = GoalsScored
        fields = '__all__'


class OpponentGoalForm(forms.ModelForm):
    class Meta:
        model = GoalsConceded
        fields = '__all__'