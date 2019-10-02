from django.db import models

# Create your models here.

class ProjectPost(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    url = models.CharField(max_length=200, blank=True, default='#')
    document = models.FileField(upload_to='documents/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title