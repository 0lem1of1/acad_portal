from django.db import models
from base.models import User,Course


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        self.user.is_professor = True
        self.user.save()
        super().save(*args, **kwargs)

class Announcement(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Announcement for {self.course.name} by {self.professor.name}"

