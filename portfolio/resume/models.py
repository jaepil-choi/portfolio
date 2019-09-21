from django.db import models

# Create your models here.

class ResumePost(models.Model):
    title = models.CharField(max_length=140)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title