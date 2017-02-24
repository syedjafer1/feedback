from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class fb(models.Model):
	Name = models.CharField(max_length=50,help_text="max. 50 characters")
	Department  = models.CharField(max_length=50)
	Comment  = models.TextField(max_length=300)
	Created_at  =models.DateTimeField(default=datetime.now)





	def __str__(self):
		return str((self.Name,self.Department,self.Comment))
		return self.Created_at
