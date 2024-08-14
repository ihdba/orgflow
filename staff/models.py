from django.db import models

# Create your models here.

from units.models import Unit


class Staff(models.Model):
    
    STAFF_POSITION = [
        ('EXECUTIVE', (
             ("CEO", "CEO"),
             ("CFO", "CFO"),
            )
        ),
         ('TECHNICAL', (
             ("SENIOR CONSULTANT", "Senior Consultant"),
             ("CONSULTANT", "Consultant"),
             ("EXTERNAL CONSULTANT", "External Consultant"),
            ) 
        ),
        ('UNKNOWN', 'Unknown'),
    ]

    position = models.CharField(max_length=25,
                  choices=STAFF_POSITION,
                  default="CONSULTANT")
    
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='assets/images/staff/', default='assets/images/staff/avatar1.jpg', blank=True)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,related_name='employee')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    
    
    class Meta:
        abstract = True
    def lower_name(self):
        return self.lower_data['fname', 'lname'].lower()
    
    def __str__(self):
        return f'{self.fname}{self.lname}'

    
    

    class Meta:
        verbose_name_plural = "Staff"
        ordering = ['unit']
    
    
    