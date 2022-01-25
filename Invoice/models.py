from django.db import models

# Create your models here.
class UserSetting(models.Model):
	user = models.CharField(max_length=100)
	projectName = models.CharField(max_length=100)
	maxWeeks = models.IntegerField()
	lastWeek = models.IntegerField()
	startDate = models.DateField()

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.projectName)