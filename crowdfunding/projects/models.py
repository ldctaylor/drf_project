from django.db import models
from django.contrib.auth import get_user_model

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    goal = models.IntegerField()
    date_created = models.DateTimeField()
    goaldate = models.DateTimeField()
    is_open = models.BooleanField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects')

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    pledge_date = models.DateTimeField()
    project = models.ForeignKey('Project',on_delete=models.CASCADE,related_name='pledges')
    supporter = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,related_name='pledges'
    )

class Condition(models.Model):
    description = models.TextField()
    conditionmet = models.BooleanField()
    pledge = models.OneToOneField(Pledge, on_delete=models.CASCADE,null=True,blank=True,related_name='condition')


