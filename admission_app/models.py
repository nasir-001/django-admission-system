from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER = (
  ('M', "Male"),
  ('F', "Female"),
)

# Create your models here.
class User(AbstractUser):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(unique=True, blank=False, error_messages={'unique': "A user with that email already exists."})
  gender = models.CharField(choices=GENDER, max_length=1, null=True)
  dob = models.DateField(null=True)

  def __str__(self):
    return self.email

  def get_full_name(self):
    return self.first_name + ' ' + self.last_name


class Admitted(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  regno = models.CharField(max_length=11, unique=True)

  def __str__(self):
    return self.regno