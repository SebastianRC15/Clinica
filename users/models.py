
from django.contrib.auth.models import User
from django.db import models
from clinica.models import Clinica

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    clinica = models.ForeignKey(Clinica, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.clinica}"
