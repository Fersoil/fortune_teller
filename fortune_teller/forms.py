from django import forms
from .models import Fortune
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class FortuneForm(forms.ModelForm):
    
    sex_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        # Add more choices here
    ]

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' '}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ' '}))
    zodiac_sign = forms.ChoiceField(choices=Fortune.ZODIAC_SIGNS, widget=forms.Select(attrs={'placeholder': ' '}))
    sex = forms.ChoiceField(choices=sex_choices, widget=forms.Select(attrs={'placeholder': ' '}))

    class Meta:
        model = Fortune
        fields = ['title', 'text', 'zodiac_sign', 'sex']
        

class RegisterForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': ' '}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' '}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': ' '}))
    password2 = forms.CharField(label='Retype your password', widget=forms.PasswordInput(attrs={'placeholder': ' '}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
