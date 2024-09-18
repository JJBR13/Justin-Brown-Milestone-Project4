from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class TourProducts(models.Model):

    class Meta:
        verbose_name_plural = 'Tour Product'

    name = models.CharField(max_length=60)
    category = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField()
    location_start = models.CharField(max_length=255, null=True, blank=True)
    location_end = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    duration = models.IntegerField(null=True, blank=True)
    four_facts = models.TextField(null=True, blank=True)
    date_available = models.DateTimeField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.name}"
