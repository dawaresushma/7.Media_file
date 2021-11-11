from django.db import models

# Create your models here.
class Instagram(models.Model):
    img=models.ImageField(upload_to='images/')
    content=models.TextField(max_length=500)
    file=models.FileField()

