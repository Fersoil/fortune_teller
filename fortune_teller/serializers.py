from rest_framework.serializers import ModelSerializer
from .models import Fortune, FortuneHistory



class FortuneSerializer(ModelSerializer):
    class Meta:
        model = Fortune
        fields = ['id', 'title', 'text', 'zodiac_sign', 'sex', "user"]


class FortuneHistorySerializer(ModelSerializer):
    class Meta:
        model = FortuneHistory
        fields = ["id", "fortune", "user"]