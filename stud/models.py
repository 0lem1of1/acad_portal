from django.db import models
from base.models import *

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  
    courses = models.ManyToManyField(Course)  
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.user.is_student = True
        self.user.save()
        super().save(*args, **kwargs)

