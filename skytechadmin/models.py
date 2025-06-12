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
    service_img = models.ImageField(upload_to='serviceImg', null=True, blank=True)
    about_service = RichTextField()
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return self.service_name
    


class OurClient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    client_logo = models.ImageField(upload_to='clients', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Enquiries(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    message = RichTextField()

    def __str__(self):
        return self.first_name
    
class Career(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=100)
    job_description = RichTextField()
    job_post_date = models.DateTimeField(auto_created=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.job_title
    
