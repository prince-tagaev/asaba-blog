from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.forms import widgets


class Profile(models.Model):
    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(
        'Фото пользователя', default='default_icon.png', upload_to='user_images')

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)
