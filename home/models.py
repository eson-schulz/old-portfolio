from django.db import models
from django.core.exceptions import ValidationError

class Job(models.Model):
	name = models.CharField(max_length=32, unique=True)

	def __unicode__(self):
		return self.name

class About(models.Model):
	LOCATIONS = (
		('1', 'First Paragraph'),
		('2', 'Second Paragraph'),
		('3', 'Footer Paragraph'),
	)

	description = models.TextField(max_length=300)
	location = models.CharField(max_length=1, choices=LOCATIONS, unique=True)

	def __unicode__(self):
		return self.description

class Project(models.Model):
	name = models.CharField(max_length=64, unique=True)
	image = models.ImageField(upload_to='/projects')
	description = models.TextField()
	source = models.CharField(max_length=128)
	kind = models.CharField(max_length=32)