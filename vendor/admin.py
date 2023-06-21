from django.contrib import admin
from vendor.models import Vendor, OpeningHour


class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'vendor_name', 'created_at', 'is_approved')
    list_display_links = ('user', 'vendor_name')
    list_editable = ('is_approved',)


class OpeningHourAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'day', 'from_hour', 'to_hour')


admin.site.register(Vendor, VendorAdmin)
admin.site.register(OpeningHour, OpeningHourAdmin)
