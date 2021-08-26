from PIL import Image
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        blank=True, null=True, default='images/default.jpg', upload_to='images/profile_pics')

    def __str__(self):
        return f"profile of: {self.user.username}"

    def save(self, *args, **kwargs):
        try:
            this = Profile.objects.get(id=self.id)
            if this.image != self.image and this.image != 'images/default.jpg':
                this.image.delete()
        except:
            pass
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if (img.height > 300) or (img.width > 300):
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
