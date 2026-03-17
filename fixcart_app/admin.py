from django.contrib import admin
from .models import RepairRequest, RepairRequestImage
from django.utils.html import format_html


class RepairRequestImageInline(admin.TabularInline):
    model = RepairRequestImage
    extra = 1
    # Show preview of uploaded image
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="80" style="border-radius:5px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"


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