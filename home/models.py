from django.db import models

class Job(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name