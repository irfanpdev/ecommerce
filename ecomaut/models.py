from django.db import models
from django.contrib.auth.models import User
  

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    token=models.CharField(max_length=200)
    forgetPasstoken=models.CharField(max_length=200)
    verify=models.BooleanField(default=False) 
    fotgetPassLinkExpStatus=models.BooleanField(default=False)
                                     

    

    