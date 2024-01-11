from rest_framework.routers import DefaultRouter
from django.urls.conf import include
from django.urls import re_path
from .viewsets import FortuneViewSet, FortuneHistoryViewSet


router = DefaultRouter()
router.register(
    r'fortunes',
    FortuneViewSet,
    basename="fortunes",
)

router.register(
    r'fortunes_histoy',
    FortuneHistoryViewSet,
    basename="fortunes_histoy",
)



urlpatterns = [
    re_path(r'', include(router.urls)),
]
# or urlpatterns = router.urls