from django.urls import path
from django.urls.conf import include
urlpatterns = [
 path('fortune_teller/', include('fortune_teller.urls_api')),
]