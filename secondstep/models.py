from django.db import models

# Create your models here.
class Object(models.Model):
    title_kor = models.CharField(max_length=50)
    title_eng = models.CharField(max_length=50)
    illust = models.ImageField(upload_to="illust", null=True, blank=True)

class UserObject(models.Model):
    photo = models.ImageField(upload_to="realimage")
    