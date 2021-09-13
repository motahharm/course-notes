from django.db import models

class course_model(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()

  def __str__(self) -> str:
      return self.title

class course_key_model(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  course = models.ForeignKey(to=course_model, on_delete=models.CASCADE)

  def __str__(self) -> str:
      return self.title