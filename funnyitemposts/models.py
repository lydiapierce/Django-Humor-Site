from django.db import models

# Create your models here.

class Funnyitempost(models.Model):
    itemname = models.CharField(max_length=100)
    itemtype = models.CharField(max_length=100)
    displayedat = models.DateTimeField('date displayed')
 
    def __unicode__(self):
    	return self.itemname

