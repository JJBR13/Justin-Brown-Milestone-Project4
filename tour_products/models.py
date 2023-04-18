from django.db import models

class TourProducts(models.Model):

    class Meta: 
        verbose_name_plural = 'Tour Product'
        
    # tour_id = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    four_facts = models.TextField(null=True, blank=True)
    date_available = models.DateTimeField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.name}"
