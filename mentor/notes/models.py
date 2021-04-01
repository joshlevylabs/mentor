from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
