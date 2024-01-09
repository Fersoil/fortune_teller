# Generated by Django 4.1 on 2024-01-08 19:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fortune_teller", "0004_userprofile_delete_profile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="birth_date",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="zodiac_sign",
            field=models.CharField(
                blank=True,
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
                max_length=20,
                null=True,
            ),
        ),
    ]