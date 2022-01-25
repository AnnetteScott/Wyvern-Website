from django.db import models

# Create your models here.
class UserSettings(models.Model):
	user = models.CharField(max_length=100)
	maxWeeks = models.IntegerField()
	lastWeeks = models.IntegerField()
	startDate = models.DateTimeField()

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.title)