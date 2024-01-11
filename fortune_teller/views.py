import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import Fortune, UserProfile, FortuneHistory
from .forms import UserInfoForm, FortuneForm, RegisterForm

import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from django.core.mail import send_mail

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def index(request):
    zodiac_sign = None
    sex = None
    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        
        logger.info("got user" + user_profile.user.__str__())
        zodiac_sign = user_profile.zodiac_sign
        sex = user_profile.sex

        fortunes_list = FortuneHistory.objects.filter(user=user_profile.user).values_list('fortune', flat=True)
        fortunes = Fortune.objects.filter(zodiac_sign=zodiac_sign, sex=sex).exclude(id__in=fortunes_list)

    elif 'zodiac_sign' in request.COOKIES and 'sex' in request.COOKIES:
        zodiac_sign = request.COOKIES['zodiac_sign']
        sex = request.COOKIES['sex']
        logger.error("got user" + zodiac_sign)
        fortunes = Fortune.objects.filter(zodiac_sign=zodiac_sign, sex=sex)
    else:
        logger.info("no user nor zodiac")
        fortunes = Fortune.objects.all()
    
    if fortunes:
        random_fortune = random.choice(fortunes)
        if request.user.is_authenticated:
            FortuneHistory.objects.create(user=request.user, fortune=random_fortune)

        context = {'fortune': random_fortune, "sex": sex, "zodiac_sign": zodiac_sign}
    else:
        context = {'fortune': None, "sex": sex, "zodiac_sign": zodiac_sign}

    return render(request, 'fortune_teller/index.html', context)

@login_required
def user_fortunes(request):
    # Fetch fortunes associated with the user
    user_fortunes = Fortune.objects.filter(user=request.user)
    return render(request, 'fortune_teller/account/login.html', {'fortunes': user_fortunes})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until it is confirmed
            user.save()

            # Create UserProfile
            profile = UserProfile(user=user)
            profile.save()

            # Send activation email
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('fortune_teller/account/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': profile.activation_key
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = RegisterForm()
    return render(request, 'fortune_teller/account/register.html', {'form': form})
    

def register_done(request):
    """Display a thank you message on the registration complete view."""
    return render(request, 'fortune_teller/account/register_done.html')


def activate(request, uidb64, token):
    user = get_object_or_404(User, pk=urlsafe_base64_decode(uidb64).decode())
    profile = get_object_or_404(UserProfile, user=user, activation_key=token)

    if profile:
        user.is_active = True
        user.save()
        # Optionally, delete the profile or the activation key
        return redirect('register_complete')
    else:
        # Invalid link
        return render(request, 'fortune_teller/account/activation_invalid.html')

def register_complete(request):
    return render(request, "fortune_teller/account/register_complete.html")


def account_info(request): # TODO
    return render(request, 'fortune_teller/account/account_info.html')

@login_required
def add_fortune(request):
    if request.method == 'POST':
        form = FortuneForm(request.POST)
        if form.is_valid():
            fortune = form.save(commit=False)
            fortune.user = request.user  # Set the user of the fortune
            fortune.save()
            return redirect('index')  # Redirect to a success page or home
    else:
        form = FortuneForm()

    return render(request, 'fortune_teller/add_fortune.html', {'form': form})


@login_required
def view_fortunes(request):
    # Fetch fortunes associated with the user
    user_fortunes = Fortune.objects.filter(user=request.user)
    return render(request, 'fortune_teller/view_fortunes.html', {'fortunes': user_fortunes})


@login_required
def edit_fortune(request, fortune_id):
    fortune = get_object_or_404(Fortune, pk=fortune_id, user=request.user)  # Ensure the user owns the fortune
    if request.method == 'POST':
        form = FortuneForm(request.POST, instance=fortune)
        if form.is_valid():
            form.save()
            return redirect('user_fortunes')  # Redirect to the fortunes list
    else:
        form = FortuneForm(instance=fortune)
    return render(request, 'fortune_teller/edit_fortune.html', {'form': form})




def user_info(request):

    if 'zodiac_sign' in request.COOKIES and 'sex' in request.COOKIES:
        zodiac_sign =request.COOKIES["zodiac_sign"]
        sex = request.COOKIES["sex"]

        context = {"zodiac_sign": zodiac_sign, "sex": sex}

        return render(request, "fortune_teller/user_info.html", context)
    else:
        if request.method == 'POST':
            form = UserInfoForm(request.POST)
            if form.is_valid():
                if request.user.is_authenticated:
                    # Save in user profile for logged-in users
                    profile = request.user.userprofile
                    profile.sex = form.cleaned_data['sex']
                    profile.zodiac_sign = form.cleaned_data['zodiac_sign']
                    profile.save()
                else:
                    # Save in cookies for anonymous users
                    response = redirect('index')  # Redirect to a desired page
                    response.set_cookie('sex', form.cleaned_data['sex'])
                    response.set_cookie('zodiac_sign', form.cleaned_data['zodiac_sign'])
                    return response
                return redirect('index')  # Redirect after saving data
        else:
            form = UserInfoForm()
        return render(request, 'fortune_teller/set_user_info.html', {'form': form})

    
@login_required
def history(request):
    if request.user.is_authenticated:
        history = FortuneHistory.objects.filter(user=request.user).order_by('-viewed_on')
        return render(request, 'fortune_teller/fortune_history.html', {'history': history})
    else:
        return redirect('login')


def clear_cookies(request):
    if request.method == 'POST':
        response = redirect('user_info')  # Redirect to a page of your choice
        response.delete_cookie('sex')      # Replace with your cookie name
        response.delete_cookie('zodiac_sign')  # Replace with your cookie name
        return response
    return redirect('user_info')  # Redirect if not POST method


def view_fortune(request, fortune_id):
    fortune = get_object_or_404(Fortune, pk=fortune_id)

    # Record the viewing in the user's history if the user is logged in
    if request.user.is_authenticated:
        FortuneHistory.objects.create(user=request.user, fortune=fortune)

    return render(request, 'fortune_teller/fortune_detail.html', {'fortune': fortune})