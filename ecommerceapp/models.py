from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
ext_validator=FileExtensionValidator(['png','jpg','jpeg'])
class ImageUpload(models.Model):
    img=models.ImageField(upload_to='img/',validators=[ext_validator])
    imgType=models.CharField(max_length=50)

    def __str__(self) :
        return self.imgType
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=150)
    category=models.CharField(max_length=150,default='')
    subcategory=models.CharField(max_length=150,default='')
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to='shop/image')

    def __str__(self) :
        return self.product_name
    
class Team(models.Model):
    name=models.CharField(max_length=80)
    desination=models.CharField(max_length=80)
    socialid_linkidin=models.CharField(max_length=150, null=True, blank=True)
    socialid_twitter=models.CharField(max_length=150 ,null=True, blank=True)
    socialid_insta=models.CharField(max_length=150, null=True, blank=True)
    socialid_facebook=models.CharField(max_length=150 ,null=True, blank=True)
    image=models.ImageField(upload_to='team/image')
    def __str__(self) :
        return self.name