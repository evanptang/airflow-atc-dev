from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Action(models.Model): 
    active = models.BooleanField(default=False)
    for_acknowledged = models.BooleanField() 
    value = models.CharField(max_length=30) 
    display_value = models.CharField(max_length=50)
    extended_value = models.CharField(max_length=300)
    datetime = models.DateTimeField(auto_now_add=True)
    user_added = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    pending_confirmation = models.BooleanField(default=True)

    def __str__(self): 
        return self.value 

  