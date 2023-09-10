from django.contrib import admin
from .models import ImageUpload,Product,Team
# Register your models here.

admin.site.register(ImageUpload)
admin.site.register(Product)
admin.site.register(Team)