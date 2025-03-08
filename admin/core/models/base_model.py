from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    agent = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        abstract = True
        app_label = 'core'