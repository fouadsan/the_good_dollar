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


class SmallPub(models.Model):
    text = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="cat_imgs/", blank=True, null=True)

    def __str__(self):
        return f"Small Pub {self.id}"


class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services_imgs')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Viewer(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return "Counter"


viewer = Viewer.objects.get_or_create()
