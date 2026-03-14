from django.contrib import admin
from .models import RepairRequest, RepairRequestImage


class RepairRequestImageInline(admin.TabularInline):
    model = RepairRequestImage
    extra = 1


@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "contact_number",
        "status",
        "created_at",
    )

    inlines = [RepairRequestImageInline]