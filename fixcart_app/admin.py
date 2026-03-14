from django.contrib import admin
from .models import RepairRequest


@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):

    list_display = ("name","category","contact_number","created_at")
    search_fields = ("name", "contact_number")
    list_filter = ("category", "created_at")