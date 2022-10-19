from django.db import models


class BrandName(models.Model):
    brand_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.brand_name


class ModelName(models.Model):
    PHONE_TYPE = (
        ('SMARTPHONE', 'Smartphone'),
        ('TABLET', 'Tablet'),
        ('WEARABLE', 'Wearable'),
        ('EARWEAR', 'Earwear'),
        ('OTHER', 'Other'),
    )
    brandName = models.ForeignKey(BrandName, on_delete=models.CASCADE,)
    model_name = models.CharField(max_length=50)
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    mobile_image = models.ImageField(upload_to='model_image/', blank=True, null=True)
    phone_type = models.CharField(max_length=20, choices=PHONE_TYPE, default='Smartphone')
    description = models.CharField(max_length=1200, blank=True, null=True)

    def __str__(self):
        return self.brandName.brand_name + ' ' + self.model_name
