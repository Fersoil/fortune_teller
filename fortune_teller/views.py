import logging
from django.shortcuts import render
from .models import Fortune, UserProfile
from .forms import UserInfoForm

import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate

from .forms import FortuneForm
from django.core.mail import send_mail

from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import UserProfile
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string

from .forms import UserInfoForm


logger = logging.getLogger(__name__)

def index(request):
    fortunes = Fortune.objects.all()
    if fortunes:
        random_fortune = random.choice(fortunes)
        context = {'fortune': random_fortune}
    else:
        context = {'fortune': None}

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


