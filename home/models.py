from django.db import models
from django.core.exceptions import ValidationError

class Job(models.Model):
	name = models.CharField(max_length=32, unique=True)

	def __unicode__(self):
		return self.name


# Limit abouts created to two
def validate_only_two_instances(obj):
	model = obj.__class__
	if (model.objects.count() > 2 and
			not obj.id in [model.id for model in model.objects.all()]):
		raise ValidationError("Can only create 2 {} instance".format(model.__unicode__))

class About(models.Model):
	description = models.TextField(max_length=300)

	def clean(self):
		validate_only_two_instances(self)

	def __unicode__(self):
		return self.description