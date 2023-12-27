# Generated by Django 4.1 on 2023-12-25 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("fortune_teller", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="fortune",
            name="sex",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                default="M",
                max_length=1,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="fortune",
            name="title",
            field=models.CharField(default="Title", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="fortune",
            name="zodiac_sign",
            field=models.CharField(
                choices=[
                    ("Aries", "Aries"),
                    ("Taurus", "Taurus"),
                    ("Gemini", "Gemini"),
                    ("Cancer", "Cancer"),
                    ("Leo", "Leo"),
                    ("Virgo", "Virgo"),
                    ("Libra", "Libra"),
                    ("Scorpio", "Scorpio"),
                    ("Sagittarius", "Sagittarius"),
                    ("Capricorn", "Capricorn"),
                    ("Aquarius", "Aquarius"),
                    ("Pisces", "Pisces"),
                ],
                default="Pisces",
                max_length=20,
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("auth_token", models.CharField(max_length=100)),
                ("is_verified", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "sex",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]