from django.db import models

class Score(models.Model):
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    identifier = models.CharField(max_length=100)
    
    