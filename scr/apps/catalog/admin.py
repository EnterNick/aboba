from django.contrib import admin

from .models import Good, Category, VisitsPerWeek

admin.site.register(Category)
admin.site.register(VisitsPerWeek)
admin.site.register(Good)
