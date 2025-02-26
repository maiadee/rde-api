from django.db import models

STATUSES = [
    ("IL", "Illustrator"),
    ("IN", "Influencer"),
    ("ST", "Stylist"),
    ("SD", "Set Designer"),
]

# Create your models here.
class Talent(models.Model):
    name = models.CharField(max_length=200, default="Unknown")
    location = models.CharField(blank=True, null=True)
    occupation = models.CharField(choices=STATUSES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

