from django.contrib import admin

from .models import Good


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    exclude = [
        'owner',
        'orders',
        'date_created',
    ]
    list_display = ['title', 'description', 'price', 'value', 'category', 'orders']
    readonly_fields = [
        'conversion_level',
        'income',
        'has_seen',
        'have_bought',
    ]

    def get_queryset(self, request):
        return super().get_queryset(request).filter(owner=request.user)

    def conversion_level(self, obj):
        try:
            return str(round(obj.orders / obj.has_seen, 3) * 100) + '%'
        except ZeroDivisionError:
            return 0
