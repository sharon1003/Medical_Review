from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):  # 建立輸入評論的資料庫
	title = models.CharField(max_length=200)
	review = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-pub_date',)

	def __str__(self):
		return self.title

class Review(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=50)
	subject = models.CharField(max_length=200)
	review = models.TextField()

	def __str__(self):
		return self.review