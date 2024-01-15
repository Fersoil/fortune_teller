from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    
    id = models.AutoField(primary_key=True)  # Primary key

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

        id = models.AutoField(primary_key=True)  # Primary key

        user = models.OneToOneField(User, on_delete=models.CASCADE)
        activation_key = models.UUIDField(default=uuid.uuid4, editable=False)
        # birth_date = models.DateField(null=True, blank=True)

        is_verified = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        sex = models.CharField(max_length=1, choices=SEX_CHOICES)  # Sex field
        zodiac_sign = models.CharField(max_length=20, choices=Fortune.ZODIAC_SIGNS, null=True, blank=True)
        is_admin = models.BooleanField(default=False)

        def __str__(self):
            return self.user.username
        

class FortuneHistory(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fortune = models.ForeignKey(Fortune, on_delete=models.CASCADE)
    viewed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} viewed {self.fortune.title}"