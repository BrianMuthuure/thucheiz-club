import datetime

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import User, Player, Contract, Coach, Contact


class ExtendedUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), required=True,
                               max_length=20)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), max_length=20)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), max_length=20)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("This username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already being used")
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email has to end with gmail.com")
        return email

    def save(self, commit=True):
        user = super(ExtendedUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class PlayerForm(forms.ModelForm):

    nationality = CountryField().formfield(
        widget=CountrySelectWidget(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Player
        fields = ('position', 'nationality', 'jersey_no', 'dob', 'image')

        widgets = {
             'position': forms.Select(attrs={
                 'class': 'form-control', 'placeholder': 'position'
             }),

             'jersey_no': forms.NumberInput(attrs=
                                            {'class': 'form-control', 'placeholder': 'jersey no'}),
             'dob': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'select date', 'type': 'date'})
        }

    def clean_dob(self):
        data = self.cleaned_data['dob']
        now = datetime.date.today()
        days_in_year = 365.2425
        age = int((now - data).days/days_in_year)
        if data >= datetime.date.today():
            raise forms.ValidationError('dob should not  be equal or greater than today')
        if age < 18:
            raise forms.ValidationError("Player should have more than 18 years")
        return data


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password ")
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class PlayerUpdateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['position', 'nationality', 'jersey_no', 'appearances', 'goals', 'clean_sheets', 'red_cards', 'yellow_card',  'image']
        widgets = {
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'jersey_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'appearances': forms.NumberInput(attrs={'class': 'form-control'}),
            'goals': forms.NumberInput(attrs={'class': 'form-control'}),
            'clean_sheets': forms.NumberInput(attrs={'class': 'form-control'}),
            'red_cards': forms.NumberInput(attrs={'class': 'form-control'}),
            'yellow_card': forms.NumberInput(attrs={'class': 'form-control'})
        }


class PlayerContractForm(forms.ModelForm):
    player = forms.ModelChoiceField(queryset=Player.objects.filter(has_contract=False),
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Contract
        fields = [
            'player', 'start_date', 'end_date', 'salary', 'buyout_clause'
        ]

        widgets = {
            'start_date': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'select date', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'select date', 'type': 'date'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'buyout_clause': forms.NumberInput(attrs={'class': 'form-control'}),
            'bonuses': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        data = self.cleaned_data
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date >= end_date:
            raise forms.ValidationError("start date should be less than end date!!!!")
        if start_date < datetime.date.today():
            raise forms.ValidationError("start date should not be less than the current date!!!!!")
        if end_date <= datetime.date.today():
            raise forms.ValidationError("End date should be greater than today")
        return data


class CoachCreationForm(forms.ModelForm):
    nationality = CountryField().formfield(
        widget=CountrySelectWidget(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Coach
        fields = ['nationality', 'dob', 'title', 'image']
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'select date', 'type': 'date'}),
            'title': forms.Select(attrs={'class': 'form-control', 'placeholder': 'position'}),
        }

    def clean_dob(self):
        data = self.cleaned_data['dob']
        now = datetime.date.today()
        days_in_year = 365.2425
        age = int((now - data).days/days_in_year)
        if data >= datetime.date.today():
            raise forms.ValidationError('dob should not  be equal or greater than today')
        if age < 30:
            raise forms.ValidationError("Coach should have more than 30 years")
        return data


class CoachUpdateForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['title', 'nationality',  'trophies', 'games', 'wins', 'losses', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'trophies': forms.NumberInput(attrs={'class': 'form-control'}),
            'games': forms.NumberInput(attrs={'class': 'form-control'}),
            'wins': forms.NumberInput(attrs={'class': 'form-control'}),
            'losses': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject']
