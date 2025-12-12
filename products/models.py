from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    rating = models.FloatField(default=0.0 , validators=[MinValueValidator(0.0),MaxValueValidator(5.0),])
    size = models.CharField(max_length=10,blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
