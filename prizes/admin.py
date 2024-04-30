from django.contrib import admin
from .models import DailyPrize, Medal, Badge


admin.site.register(DailyPrize)
admin.site.register(Medal)
admin.site.register(Badge)
