from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_contractor = models.BooleanField(default=False)
    vendor_name = models.CharField(max_length=100)
    contractor_name = models.CharField(max_length=100)

class Vendor(models.Model):
    user = models.OneToOneField(Users, on_delete = models.CASCADE, primary_key = True)
    vendor_email = models.EmailField(max_length=25)
    vendor_address = models.CharField(max_length=150)
    vendor_contact = models.IntegerField(max_length=20, null=True)
    vendor_description = models.CharField(max_length=255)
    year_of_experience = models.IntegerField(max_length=255, null=True)
    currently_working = models.CharField(max_length=255)
    vendor_Img = models.ImageField(upload_to='Vendor_images/')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Vendor " + str(self.user)
    

class Contractor(models.Model):
    user = models.OneToOneField(Users, on_delete = models.CASCADE, primary_key = True)
    contractor_email = models.EmailField(max_length=25)
    contractor_address = models.CharField(max_length=150)
    contractor_contact = models.IntegerField(max_length=20, null=True)
    contractor_description = models.CharField(max_length=255)
    year_of_experience = models.IntegerField(max_length=255, null=True)
    project_ongoing = models.IntegerField(max_length=255, null=True)
    projects_completed = models.IntegerField(max_length=255, null=True)
    number_of_successful_clients = models.IntegerField(
        max_length=255, null=True)
    rating = models.IntegerField(max_length=255, null=True)
    contact_number_of_previous_client = models.IntegerField(
        max_length=30, null=True)
    contractor_Img = models.ImageField(upload_to='Contractor_images/', blank=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Contractor " + str(self.user)


class Contact_us(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    message = models.CharField(max_length=100)
    
    def __str__(self):
        return "Complain By " + str(self.name)
    
    class Meta:
        verbose_name = 'Complain / Contact info'
        verbose_name_plural = 'Complain / Contact info'
