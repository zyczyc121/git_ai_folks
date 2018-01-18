from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Scholar(models.Model):
    GENDER_CHOICE = {
        (0, 'Male'),
        (1, 'Female')
    }

    guid = models.CharField(max_length = 50, db_index = True, null = True)
    classification = models.CharField(max_length = 30, blank = True, null = True)
    name = models.CharField(max_length = 100, null = True)
    sex = models.IntegerField(choices = GENDER_CHOICE, null = True)
    birthday = models.DateTimeField(null = True)
    degree = models.CharField(max_length = 1, null = True)
    title = models.CharField(max_length = 1, null = True)
    graduateschool = models.CharField(max_length = 500, null = True)
    subject = models.CharField(max_length = 500, null = True)
    introduction = models.TextField(blank = True, null = True)
    achievement = models.TextField(blank = True, null = True)
    affiliation = models.TextField(blank = True, null = True)
    nationality = models.CharField(max_length = 30, null = True)
    email = models.CharField(max_length = 100, null = True)
    homepage = models.TextField(null = True)
    photourl = models.TextField(null = True)
    lastmodified = models.DateTimeField(null = True)
    keywords = models.TextField(null = True)
    position = models.CharField(max_length = 100, null = True)
    rank = models.IntegerField(null = True)
    focus = JSONField(null = True, default=None)
    statistics = JSONField(null = True, default=None)
    
class Tag(models.Model):
    title = models.CharField(max_length = 60)
    members = models.ManyToManyField(Scholar, through = 'Label')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    def __str__(self):
        return self.title

class Label(models.Model):
    scholar = models.ForeignKey(Scholar, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

class Paper(models.Model):
    scholar = models.ForeignKey(Scholar, on_delete=models.CASCADE)
    info_json = JSONField(null = True, default = None)


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length = 20, null = True, default = '我的人才库')
    scholar = models.ManyToManyField(Scholar)
    
