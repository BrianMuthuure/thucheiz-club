import datetime

from django import forms
from fixtures.models import Fixture


class FixtureCreationForm(forms.ModelForm):

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError('Fixture date should not be less than today!!')
        return date

    class Meta:
        model = Fixture
        fields = ['title', 'opponent', 'image', 'stadium', 'time', 'date']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'dob', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': '00:00:00'}),
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'stadium': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FixtureUpdateForm(forms.ModelForm):

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < datetime.date.today():
            raise forms.ValidationError("Fixture date cannot be less than today !!!!!")
        return date

    class Meta:
        model = Fixture
        fields = ['title', 'opponent', 'image', 'stadium', 'date', 'time']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'stadium': forms.TextInput(attrs={'class': 'form-control'}),
        }