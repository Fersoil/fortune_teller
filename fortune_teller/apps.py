from django.apps import AppConfig


class FortuneTellerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fortune_teller"

    # def ready(self):
    #     import fortune_teller.signals
