from django.db import models

# Create your models here.

class Instance(models.Model):

    #instances = models.

    objects = models.User()

    def __str__(self):
        return str(self.pk) + ": " + self.name

'''
class Account(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password
'''