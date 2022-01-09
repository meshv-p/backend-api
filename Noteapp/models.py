from django.db import models

# Create your models here.
class Notes(models.Model):
    # sno = models.AutoField()
    title = models.CharField(max_length=50)
    desc = models.TextField()
    time=models.TimeField(auto_now=True)
    # img = models.ImageField(upload_to='static1/img', height_field=None, width_field=None, max_length=None,default=None)


    def __str__(self):
        return self.title


