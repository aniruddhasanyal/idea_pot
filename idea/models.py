from django.db import models
from django.contrib.auth.models import User
import json

class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Idea(models.Model):
    author = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    title = models.CharField(max_length=100)
    description = models.TextField()
    repository = models.URLField(max_length=150)
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def settags(self, x):
        self.tags = json.dumps(x)

    def gettags(self):
        return json.loads(self.tags)
