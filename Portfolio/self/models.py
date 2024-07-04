from django.db import models

# Create your models here.
class Contact(models.Model):
    FRONT_END = 'Front-End'
    BACK_END = 'Back-End'
    FULL_STACK = 'Full_Stack'
    POSITION_CHOICES = [
        (FRONT_END, 'Front-End'),
        (BACK_END, 'Back-End'),
        (FULL_STACK, 'Full Stack'),
    ]

    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)  # Use EmailField for email validation
    Phone = models.CharField(max_length=15)  # Updated max_length to allow for international numbers
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.First_Name
