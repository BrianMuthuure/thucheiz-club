import datetime


from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import User, Player, Contract, Coach, Contact, Injury, DeletedPlayer


class ExtendedUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=
                                                      {'class': 'form-control', 'type': 'text'}),
                               required=True,
                               max_length=20)
    first_name = forms.CharField(widget=forms.TextInput(attrs=
                                                        {'class': 'form-control', 'input type': 'text'}),
                                 max_length=20, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs=
                                                       {'class': 'form-control', 'input type': 'text'}),
                                max_length=20, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs=
                                                     {'class': 'form-control', 'type': 'email'}),
                             required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=
                                                           {'class': 'form-control', 'type': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=
                                                           {'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not str(first_name).isalpha():
            raise forms.ValidationError("first name should be in letters!!!!")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not str(last_name).isalpha():
            raise forms.ValidationError("last name should be in letters!!!!")
        return last_name

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


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), required=True,
                               max_length=20)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}), required=True)

    class Meta:
        model = User
        fields = ('username', 'email')


class PlayerForm(forms.ModelForm):

    country = CountryField().formfield(
        widget=CountrySelectWidget(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Player
        fields = ('position', 'country', 'jersey_no', 'dob', 'image')

        widgets = {
             'position': forms.Select(attrs={
                 'class': 'form-control', 'placeholder': 'position'
             }),

             'jersey_no': forms.Select(attrs=
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
    country = CountryField().formfield(
        widget=CountrySelectWidget(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Player
        fields = ['position', 'country', 'jersey_no', 'appearances', 'goals', 'clean_sheets', 'red_cards', 'yellow_card',  'image']
        widgets = {
              'position': forms.Select(attrs={
                 'class': 'form-control', 'placeholder': 'position'}),
            'jersey_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'appearances': forms.NumberInput(attrs={'class': 'form-control'}),
            'goals': forms.NumberInput(attrs={'class': 'form-control'}),
            'clean_sheets': forms.NumberInput(attrs={'class': 'form-control'}),
            'red_cards': forms.NumberInput(attrs={'class': 'form-control'}),
            'yellow_card': forms.NumberInput(attrs={'class': 'form-control'})
        }


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
    nationality = CountryField().formfield(
        widget=CountrySelectWidget(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Coach
        fields = ['title', 'nationality',  'trophies', 'draws', 'wins', 'losses', 'image']
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control', 'placeholder': 'position'}),
            'trophies': forms.NumberInput(attrs={'class': 'form-control'}),
            'draws': forms.NumberInput(attrs={'class': 'form-control'}),
            'wins': forms.NumberInput(attrs={'class': 'form-control'}),
            'losses': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PlayerContractCreationForm(forms.ModelForm):
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

    class Meta:
        model = Contract
        fields = ['start_date', 'end_date', 'salary', 'buyout_clause']
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'select date', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'select date', 'type': 'date'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'buyout_clause': forms.NumberInput(attrs={'class': 'form-control'})
        }


class PlayerContractUpdateForm(forms.ModelForm):

    disabled_fields = ('player',)

    class Meta:
        model = Contract
        fields = '__all__'
        widgets = {
            'player': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'select date', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'select date', 'type': 'date'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'buyout_clause': forms.NumberInput(attrs={'class': 'form-control'})
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

    def __init__(self, *args, **kwargs):
        super(PlayerContractUpdateForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject']


class InjuryForm(forms.ModelForm):
    class Meta:
        model = Injury
        fields = '__all__'


class InjuryUpdateForm(forms.ModelForm):
    class Meta:
        model = Injury
        fields = '__all__'
        exclude = ('player',)


class DeletePlayerForm(forms.ModelForm):
    class Meta:
        model = DeletedPlayer
        fields = '__all__'
