from django.db import models
from django.utils.html import mark_safe


# Banner
class Banner(models.Model):
    img = models.ImageField(upload_to="banner_imgs/")
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text


# Color
class Color(models.Model):
    title = models.CharField(max_length=50)
    color_code = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Colors'

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="depart_imgs/", blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="brand_imgs/")

    class Meta:
        verbose_name_plural = 'Brands'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name


# Size
class Size(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.title


# Product Model
class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    detail = models.TextField()
    specs = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


# Product Attribute
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="product_imgs/", null=True)

    class Meta:
        verbose_name_plural = 'ProductAttributes'

    def __str__(self):
        return self.product.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))