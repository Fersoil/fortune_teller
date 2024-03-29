from django import forms
from .models import Fortune, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import SetPasswordForm



class FortuneForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' '}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ' '}))
    zodiac_sign = forms.ChoiceField(choices=Fortune.ZODIAC_SIGNS, widget=forms.Select(attrs={'placeholder': ' '}))
    sex = forms.ChoiceField(choices=Fortune.SEX_CHOICES, widget=forms.Select(attrs={'placeholder': ' '}))

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

    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with that username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['sex', 'zodiac_sign']

class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        #'placeholder': 'Password',
    }))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        #'placeholder': 'Confirm Password',
    }))