from django.db import models

# Create your models here.
from staff.models import Staff
from units.models import Unit

class Project(models.Model):
    
    PROJECT_STATUS = (
        ("ACTIVE", "Active"),
        ("COMPLETED", "Completed"),
        ("CANCELED", "Canceled"),
        ("ON HOLD", "On Hold")
    )
    
    PROJECT_PHASE = (
        ("INITIATED", "Initiated"),
        ("PLAN & PREPARE", "Plan & Prepare"),
        ("BUILD & MANAGE", "Build & Manage"),
        ("CLOSE & SUSTAIN", "Close & Sustain")
    )
    
    PROJECT_HEALTH = (
        ('ORANGE', 'To be started'),
        ('GREEN', 'On Track'),
        ('YELLOW', 'Risk Identified'),
        ('RED', 'Off Track')
    )
    
    name= models.CharField(max_length=120)
    start_date = models.DateField(auto_now_add=True)
    date_finish = models.DateField(null=True, blank=True)
    status = models.CharField(choices=PROJECT_STATUS, default="ACTIVE")
    phase = models.CharField(choices=PROJECT_PHASE, default="INITIATED")
    health = models.CharField(choices=PROJECT_HEALTH, default="GREEN")
    manager = models.ForeignKey(Staff, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
         return f'{self.name} {self.manager}'
    
    
    
    
  # To be added ProjectTeam model. 
  # Many to Many relation.
  # One employee can be member in many projects 
  # and one project has many employees
    