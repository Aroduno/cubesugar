from django.db import models

class UploadImage(models.Model):
    image = models.ImageField(upload_to='img/')
    path = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.path

class Image(models.Model):
    path = models.CharField(max_length=200)
    def __str__(self):
        return self.path
