from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid

class Fortune(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    ZODIAC_SIGNS = [
        ('Aries', 'Aries'),
        ('Taurus', 'Taurus'),
        ('Gemini', 'Gemini'),
        ('Cancer', 'Cancer'),
        ('Leo', 'Leo'),
        ('Virgo', 'Virgo'),
        ('Libra', 'Libra'),
        ('Scorpio', 'Scorpio'),
        ('Sagittarius', 'Sagittarius'),
        ('Capricorn', 'Capricorn'),
        ('Aquarius', 'Aquarius'),
        ('Pisces', 'Pisces'),
    ]
    
    title = models.CharField(max_length=100)  # The fortune title
    text = models.TextField(max_length=1000)  # The fortune text
    created_at = models.DateTimeField(auto_now_add=True)  # Date when the fortune was created
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)  # Reference to the User model
    zodiac_sign = models.CharField(max_length=20, choices=ZODIAC_SIGNS)  # Zodiac sign
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)  # Sex field

    def __str__(self):
        return self.title


class UserProfile(models.Model):
        SEX_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        ]


        user = models.OneToOneField(User, on_delete=models.CASCADE)
        activation_key = models.UUIDField(default=uuid.uuid4, editable=False)
        birth_date = models.DateField(null=True, blank=True)

        is_verified = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        sex = models.CharField(max_length=1, choices=SEX_CHOICES)  # Sex field

        def __str__(self):
            return self.user.username
