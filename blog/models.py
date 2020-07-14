from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date  = models.DateTimeField(auto_now_add=True)
    body  = models.CharField(max_length=1000)
    def __str__(self):
        return self.title

class Game(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    release_date = models.DateField()
    def __str__(self):
        return self.name