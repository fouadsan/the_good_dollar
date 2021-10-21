from django.contrib import admin

from .models import Banner, SmallPub, Service, Viewer


class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')


admin.site.register(Banner, BannerAdmin)


admin.site.register(SmallPub)

admin.site.register(Service)


class ViewerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True

    list_display = ('count',)


admin.site.register(Viewer, ViewerAdmin)
