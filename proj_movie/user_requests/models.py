from django.db import models

class RequestCounter(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.count)
