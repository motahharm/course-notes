from django.contrib import admin
from . import models

admin.site.register(models.course_model)
admin.site.register(models.course_key_model)