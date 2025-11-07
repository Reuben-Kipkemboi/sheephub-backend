from django.db import models
from datetime import date

class Breed(models.Model):
    name = models.CharField(max_length=100, unique=True)
    origin = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



class Sheep(models.Model):
    name = models.CharField(max_length=100)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, related_name='sheep')
    date_of_birth = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    health_status = models.CharField(max_length=100, default='Healthy')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.breed.name})"

    @property
    def age_in_months(self):
        today = date.today()
        months = (today.year - self.date_of_birth.year) * 12 + (today.month - self.date_of_birth.month)
        if today.day < self.date_of_birth.day:
            months -= 1
        return months

    @property
    def age_in_years(self):
        return self.age_in_months / 12
