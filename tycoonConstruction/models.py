import email
from pickle import TRUE
from django.db import models
from accounts.models import Vendor, Contractor
# Manualy Added
# from django.contrib.auth.models import User

# bidding models
class bidContractor(models.Model):
    first_name=models.CharField(max_length=120, null= True)
    last_name=models.CharField(max_length=120, null= True)
    mobile_no=models.IntegerField(max_length=20 ,null=True)
    email=models.EmailField(max_length=50,null=True)
    project_address=models.CharField(max_length=200,null=True)
    desc=models.CharField(max_length=300,null=True)
    project_budget = models.IntegerField(max_length=200, null=True)
    mini_vendors = models.IntegerField(max_length=200, null=True)
    meeting_date=models.DateField()
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now_add=True)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return "%s" %(self.first_name) + " Requested for project"
    
    class Meta:
        verbose_name = 'Bid / Hire Contractor'
        verbose_name_plural = 'Bid / Hire Contractor'

class bidVendor(models.Model):
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)
    mobile_no = models.IntegerField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    project_address = models.CharField(max_length=200, null=True)
    projectbudget = models.IntegerField(max_length=200, null=True)
    desc = models.CharField(max_length=300, null=True)
    meeting_date = models.DateField()
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s" % (self.first_name) + " Requested for project"

    class Meta:
        verbose_name = 'Bid / Hire Vendor'
        verbose_name_plural = 'Bid / Hire Vendor'



# cost estimation model


class Estimation(models.Model):
    brickCost = models.IntegerField(help_text="Brick Cost")
    sandCost = models.IntegerField(help_text="Sand Cost")
    cementCost = models.IntegerField(help_text="Cement Cost")
    labourCost = models.IntegerField(help_text="Labour Cost")
    steelCost = models.IntegerField(help_text="Steel Cost")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Basic Construction Material Prices"
    
    class Meta:
        verbose_name = 'Update Material Costs'
        verbose_name_plural = 'Update Material Costs'
        
        
# vendor to contractor request
class VtoC_req(models.Model):
    name = models.CharField(max_length=30)
    v_email=models.EmailField(max_length=50,null=True)
    year_of_experience = models.IntegerField()
    projects_done = models.IntegerField()
    rating = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='vtoc/')
    contractor = models.ForeignKey(
        Contractor, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return "As Vendor " + self.name + " -> Requested to Contractor for Job"
    
    class Meta:
        verbose_name = 'Vendor To Contractor Request'
        verbose_name_plural = 'Vendor To Contractor Request'

# Accept Cleint Request from Contractor
class Accept_request(models.Model):
    msg=models.CharField(max_length=200)
    projects = models.ForeignKey(
        bidContractor, on_delete=models.CASCADE)
    bool = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Contractor Message is " + self.msg
    
    class Meta:
        verbose_name = 'Accept Client Request (Contractor)'
        verbose_name_plural = 'Accept Client Request (Contractor)'

# Accept Vendor Request from Contractor
class Accept_vendor_request(models.Model):
    mesg=models.CharField(max_length=200)
    vtoc_req = models.ForeignKey(
        VtoC_req, on_delete=models.CASCADE)
    bool = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Contractor Message is " + self.mesg

    class Meta:
        verbose_name = 'Accept Vendor Request (Contractor)'
        verbose_name_plural = 'Accept Vendor Request (Contractor)'

# Accept Client Request from Vendor
class Vendor_accept(models.Model):
    v_mesg=models.CharField(max_length=200)
    projects = models.ForeignKey(
        bidVendor, on_delete=models.CASCADE)
    bool = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Vendor Message is " + self.v_mesg

    class Meta:
        verbose_name = 'Accept Client Request (Vendor)'
        verbose_name_plural = 'Accept Client Request (Vendor)'
    

