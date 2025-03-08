from django.db import models
from .base_model import BaseModel
class ScoreHistory(BaseModel):
    
    user = models.ForeignKey('Prospect',
                                related_name='score_history',
                                on_delete=models.CASCADE)
    
    score = models.IntegerField()
    
    
    class Meta:
        app_label = 'core'
        db_table = 'score_history'