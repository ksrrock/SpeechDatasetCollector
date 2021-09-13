from django.db import models

# Create your models here.
class Dataset(models.Model):
    audio=models.FileField(blank=True)
    transcript=models.CharField(max_length=500,blank=True,null=True)
    def __str__(self) -> str:
        return str(self.transcript)




