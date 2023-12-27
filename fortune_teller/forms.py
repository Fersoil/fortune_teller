from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Fortune


class FortuneForm(forms.ModelForm):
    
    sex_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        # Add more choices here
    ]

    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    zodiac_sign = forms.ChoiceField(choices=Fortune.ZODIAC_SIGNS)
    sex = forms.ChoiceField(choices=Fortune.SEX_CHOICES)

    class Meta:
        model = Fortune
        fields = ['title', 'text', 'zodiac_sign', 'sex']
        


class RegisterForm(UserCreationForm):

    email = forms.EmailField()  # Adding an email field
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
