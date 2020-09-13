from django.db import models


class Student(models.Model):
    username = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, unique=True)
    
    

    def __str__(self):
        return self.username + "- a student"