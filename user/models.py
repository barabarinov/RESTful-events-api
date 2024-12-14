from django.contrib.auth.models import AbstractUser


#  Replacing default user for future potential user modifications
class User(AbstractUser):
    pass
