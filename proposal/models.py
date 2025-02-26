from django.db import models
from talent.models import Talent
from users.models import User

class Proposal(models.Model):
    # Status choices
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("under_offer", "Under Offer"),
    ]

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='submitted_proposals')
    talent = models.ForeignKey(to=Talent, on_delete=models.CASCADE, related_name='received_proposals')
    brand = models.CharField(max_length=250)
    project_title = models.CharField(max_length=250)
    project_proposal = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")  # Added status field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project_title} - {self.talent.name} ({self.get_status_display()})"
