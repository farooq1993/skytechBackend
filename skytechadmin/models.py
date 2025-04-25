from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Mainservice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    main_service_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return self.main_service_name
    

class Subservicename(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    main_service_name = models.ForeignKey(Mainservice, on_delete=models.CASCADE, null=True, blank=True)
    service_name = models.CharField(max_length=200, null=True, blank=True)
    about_service = RichTextField()
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return self.service_name
    


class OurClient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    client_logo = models.ImageField(upload_to='clients', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)