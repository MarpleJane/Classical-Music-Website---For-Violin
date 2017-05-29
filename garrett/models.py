from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    passwrd = models.CharField(max_length=50, blank=False, null=False)


class authors(models.Model):
    singerID = models.CharField(max_length=10)
    name = models.CharField(max_length=100, blank=False, null=False)
    nation = models.CharField(max_length=100)
    birth = models.CharField(max_length=50)
    intro = models.TextField(max_length=500)
    picture = models.ImageField(upload_to='garrett', null=True)


class songs(models.Model):
    songID = models.IntegerField(blank=False, null=False)
    songName = models.CharField(max_length=120, blank=False, null=False)
    singerID = models.CharField(max_length=10, blank=False, null=False)
    songURL = models.CharField(max_length=100, blank=False, null=False)
    info = models.CharField(max_length=100, blank=False, null=False)


class commentPost(models.Model):
    songID = models.IntegerField(blank=False, null=False)
    account = models.CharField(max_length=20, blank=False, null=False)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp',)
