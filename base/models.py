from django.db import models
from django.contrib.auth.models import AbstractUser
from prof.models import Professor

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max=10)
    year = models.IntegerField()
    owner = models.ForeignKey(Professor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_CDC = models.BooleanField(default=False)