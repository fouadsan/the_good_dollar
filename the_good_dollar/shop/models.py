from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User


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
    image = models.ImageField(upload_to="cat_imgs/", blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'subcategories'

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
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)
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
        verbose_name_plural = 'Product Attributes'

    def __str__(self):
        return self.product.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))


# Product Review
RATING=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')
)
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_text = models.TextField()
    review_rating = models.CharField(choices=RATING, default="1", max_length=150)

    class Meta:
        verbose_name_plural='Reviews'

    def get_review_rating(self):
        return self.review_rating