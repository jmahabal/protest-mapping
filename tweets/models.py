from django.db import models

# Create your models here.

class Tweet(models.Model):
	tweettest = models.CharField(max_length=200)
	def __str__(self):
		return self.tweettest

