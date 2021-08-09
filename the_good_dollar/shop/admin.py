from django.contrib import admin

from .models import Banner, Category, Brand, Color, Size, Product, ProductAttribute


class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')


admin.site.register(Banner, BannerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Brand, BrandAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_bg')


admin.site.register(Color, ColorAdmin)

admin.site.register(Size)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category',
                    'brand', 'status', 'is_featured')
    list_editable = ('status', 'is_featured')


admin.site.register(Product, ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'product', 'price', 'color', 'size')


admin.site.register(ProductAttribute, ProductAttributeAdmin)
