from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Banner, Category, Subcategory, Brand, Color, Size, Product, ProductAttribute, ProductReview


class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')


admin.site.register(Banner, BannerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'color')


admin.site.register(Category, CategoryAdmin)


admin.site.register(Subcategory)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')


admin.site.register(Brand, BrandAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_bg')


admin.site.register(Color, ColorAdmin)

admin.site.register(Size)


class ProductSummerAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'subcategory',
                    'brand', 'status', 'is_featured')
    list_editable = ('status', 'is_featured')

    summernote_fields = 'specs'


admin.site.register(Product, ProductSummerAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'product', 'price', 'color', 'size')


admin.site.register(ProductAttribute, ProductAttributeAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'review_text', 'get_review_rating')


admin.site.register(ProductReview, ProductReviewAdmin)
