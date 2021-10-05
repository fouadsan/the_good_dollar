from django.contrib import admin

from .models import SmallPub, Viewer

admin.site.register(SmallPub)


class ViewerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = ('count',)


admin.site.register(Viewer, ViewerAdmin)
