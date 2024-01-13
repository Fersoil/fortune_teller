from django.contrib import admin
from .models import Fortune, UserProfile, FortuneHistory

# Register your models here.


admin.site.register(Fortune)
admin.site.register(UserProfile)
admin.site.register(FortuneHistory)