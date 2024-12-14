from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class website_header(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ImageField(upload_to='website_header/',blank=True,null=True)
    is_active = models.BooleanField(default=False)

