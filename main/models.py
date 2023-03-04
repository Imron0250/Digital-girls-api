from django.db import models

class Aplication(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date = models.DateField()
    email = models.EmailField()
    adress = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)


class Info(models.Model):
    logo = models.ImageField()
    web_site = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.EmailField()
    adress = models.CharField(max_length=255)
    instagramm = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    map = models.CharField(max_length=255)

class Import_screen(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

class About_project(models.Model):
    photo = models.ImageField()
    text = models.CharField(max_length=255)


class Direction_more(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)

class Direction_about(models.Model):
    photo = models.ImageField()
    text = models.TextField()

class Tasks(models.Model):
    title = models.CharField(max_length=255)
    numer = models.IntegerField()

class Result(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)

