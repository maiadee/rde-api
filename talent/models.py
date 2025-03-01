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
    location = models.CharField(max_length=200, blank=True, null=True)
    occupation = models.CharField(choices=STATUSES, max_length=2)
    description = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to="talent_profiles/", blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

# images will be saved inside /media/talent_profiles/ - single profile image per talent

class TalentImage(models.Model):
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="talent_gallery/")  # stores multiple images

    def __str__(self):
        return f"Image for {self.talent.name}"
