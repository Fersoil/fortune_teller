from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import FortuneSerializer, FortuneHistorySerializer
from .models import Fortune, FortuneHistory
from rest_framework_xml.renderers import XMLRenderer



class FortuneViewSet(ModelViewSet):
    serializer_class = FortuneSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
            queryset = Fortune.objects.all()
            zodiac_sign = self.request.query_params.get('zodiac_sign')
            sex = self.request.query_params.get('sex')
            id = self.request.query_params.get("id")

            if id is not None:
                queryset = queryset.filter(id=id)
            if zodiac_sign is not None:
                queryset = queryset.filter(zodiac_sign=zodiac_sign)
            if sex is not None:
                queryset = queryset.filter(sex=sex)

            return queryset
 


class FortuneHistoryViewSet(ModelViewSet):
    queryset = FortuneHistory.objects.all().order_by('-viewed_on')
    serializer_class = FortuneHistorySerializer
    permission_classes = [IsAuthenticated]