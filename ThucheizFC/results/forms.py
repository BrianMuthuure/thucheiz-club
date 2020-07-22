from django import forms
import datetime
from results.models import Result


class ResultCreationForm(forms.ModelForm):

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date > datetime.date.today():
            raise forms.ValidationError('Match date should not be greater than today !!!!')
        return date

    class Meta:
        model = Result
        fields = ['result_type', 'club_score', 'opponent', 'opponent_score', 'opponent_image', 'date']
        widgets = {
            'result_type': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'club_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
