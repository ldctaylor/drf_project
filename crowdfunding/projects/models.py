from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    goal = models.IntegerField()
    date_created = models.DateTimeField()
    goaldate = models.DateTimeField()
    is_open = models.BooleanField()
    owner = models.CharField(max_length=200)
