from django.contrib import admin
from .models import Klines
# Register your models here.


class KlineAdmin(admin.ModelAdmin):
	pass

admin.site.register(Klines, KlineAdmin)