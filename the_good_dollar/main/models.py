from django.db import models


class SmallPub(models.Model):
    text = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="cat_imgs/", blank=True, null=True)

    def __str__(self):
        return f"Small Pub {self.id}"


class Viewer(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return "Counter"


viewer = Viewer.objects.get_or_create()
