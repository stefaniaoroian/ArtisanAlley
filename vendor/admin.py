from django.contrib import admin
from vendor.models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'vendor_name', 'created_at')
    list_display_links = ('user', 'vendor_name')

admin.site.register(Vendor, VendorAdmin)
