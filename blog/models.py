from email.policy import default
from pickle import FALSE
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, default='About me', editable=FALSE)
    description = models.CharField(max_length=500, default='I am Fanilo, a developer from Onja Madagascar', editable=FALSE)

    def __str__(self):
        return self.name + ' ' + self.description
