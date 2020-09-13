from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Student

class MyBackend(BaseBackend):
    
    def authenticate(self, request, username=None, password=None):
        try:
            user = Student.objects.get(username=username)
            #print(user)
        except User.DoesNotExist:
            return None   
        return user
        