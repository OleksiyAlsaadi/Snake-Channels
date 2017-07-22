from django.db import models

# Create your models here.
class Suggestion(models.Model):
    suggestion = models.CharField(max_length=140)

    def __str__(self):
        return self.suggestion
