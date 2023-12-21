from django.db import models
from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager


from django.db import models
 # Import the Lancer model from the 'lancer' app
from django.db import models


from datetime import datetime
from django.utils import timezone
# Create your models here.
from .manager import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta

import uuid


class User(AbstractUser):
    phone_number = models.CharField(max_length=12,unique=True)
    
    is_phone_verified = models.BooleanField(default=False)
   
    otp = models.CharField(max_length=6, blank=True, null=True)
    
    
    USERNAME_FIELD ='phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    
    
from django.db import models
from django.conf import settings
import uuid
from django.utils import timezone

class Lancer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Profiles')
    phone_number = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    uid = models.UUIDField(default=uuid.uuid4)
    otp = models.CharField(max_length=100)
    pfp = models.ImageField(upload_to="lancer_pics")
    is_superuser = models.BooleanField(default=True)

class Projects(models.Model):
    STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('notpaid', 'Not Paid'),
    )
    LANCER_CHOICES = (
        (True, 'Yes'),
        (False, 'No'),
    )

    lancer = models.ForeignKey(Lancer, on_delete=models.CASCADE, related_name='clients')
    title = models.CharField(max_length=100)
   
    cost = models.CharField(max_length=100)
    message = models.CharField(max_length=300, default='')
    files = models.FileField(upload_to='lancer_project_files/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='notpaid')
    date_added = models.DateTimeField(default=timezone.now)
   
    link = models.SlugField(unique=True)
    razor_pay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_signature = models.CharField(max_length=100, null=True, blank=True)
    allow_without_pay = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.status:
            self.status = 'notpaid'
        super(Projects, self).save(*args, **kwargs)


from uuid import uuid4
class TempFile(models.Model):
    file = models.FileField(upload_to='uploads/')  # Define the field to store the file
    unique_id = models.UUIDField(default=uuid4, editable=False, unique=True)
    number=models.CharField(max_length=100)