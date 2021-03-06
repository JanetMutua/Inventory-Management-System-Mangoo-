from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    # create a one to many relationship with each user and profile.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='deault.jpg', upload_to='profile_pics')
