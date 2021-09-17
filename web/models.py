from django.db import models
from django.contrib.auth.models import User


class course_model(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  author = models.ForeignKey(to=User, on_delete=models.CASCADE)

  def __str__(self) -> str:
      return self.title

class lesson_model(models.Model):
  key = models.TextField()
  value = models.TextField()
  course = models.ForeignKey(to=course_model, on_delete=models.CASCADE)

  def __str__(self) -> str:
      return self.key