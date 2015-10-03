from django.contrib import admin

from .models import AccessKey


class AccessKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'created_at', 'expired',)

admin.site.register(AccessKey, AccessKeyAdmin)
