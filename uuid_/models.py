from django.db import models


# Create your models here.
class UUID(models.Model):
    uuid_str = models.CharField(max_length=10000)
    time_stamp = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.uuid_str
