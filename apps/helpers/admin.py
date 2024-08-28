from django.contrib import admin
from .models import Helpers, HelperTypes

class HelpersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'helper_type', 'phone', 'cost', 'available', 'address', 'zipcode', 'created_at')
    search_fields = ('name', 'phone', 'helper_type', 'cost', 'address', 'zipcode', 'available')
    list_filter = ('zipcode', 'helper_type', 'cost', 'available')

class HelperTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Helpers, HelpersAdmin)
admin.site.register(HelperTypes, HelperTypesAdmin)