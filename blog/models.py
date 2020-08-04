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


class Company_Category(models.Model):
    Company = models.CharField(max_length=30)
    def __str__(self):
        return '%s' % (self.Company)  

class BU_Category(models.Model):
    BU = models.CharField(max_length=30)
    def __str__(self):
        return '%s' % (self.BU)  

class NIP(models.Model):
    JobID = models.CharField(max_length=100)
    Company_ID = models.ForeignKey(Company_Category, on_delete=models.CASCADE)
    # BU_ID = models.ForeignKey(BU_Category, on_delete=models.CASCADE)
    pub_date = models.DateField()
    def __str__(self):
        return self.JobID
    class Meta:
        ordering = ['JobID']



