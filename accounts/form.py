from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import Users,Vendor,Contractor, Contact_us

class VendorSignUpForm(UserCreationForm):
    vendor_name = forms.CharField(label="Full Name", widget=forms.TextInput(
        {"placeholder": "Full Name"}),  required=True)
    
    vendor_email = forms.EmailField(widget=forms.TextInput(
        {"placeholder": "Your Email"}), required=True)
    
    vendor_address = forms.CharField(widget=forms.TextInput(
        {"placeholder": "Current Address"}), required=True)
    
    vendor_contact = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "Current Contact Number"}), required=True)
    
    vendor_description = forms.CharField(widget=forms.TextInput(
        {"placeholder": "Description about your work... "}), label="About Me / Description", required=True)
    
    year_of_experience = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "Years Of Experience"}), required=True)
    
    currently_working = forms.CharField(
        widget=forms.TextInput({"placeholder": "Yes / No"}), required=True)
    
    vendor_Img = forms.ImageField(label="Your Image")

    class Meta(UserCreationForm.Meta):
        model = Users
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        user.vendor_name = self.cleaned_data.get('vendor_name')
        user.save()
        vendor = Vendor.objects.create(user=user)
        vendor.vendor_email=self.cleaned_data.get('vendor_email')
        vendor.vendor_address=self.cleaned_data.get('vendor_address')
        vendor.vendor_contact=self.cleaned_data.get('vendor_contact')
        vendor.vendor_description=self.cleaned_data.get('vendor_description')
        vendor.year_of_experience = self.cleaned_data.get('year_of_experience')
        vendor.currently_working = self.cleaned_data.get('currently_working')
        vendor.vendor_Img = self.cleaned_data.get('vendor_Img')
        vendor.save()
        return user

class ContractorSignUpForm(UserCreationForm):
    contractor_name = forms.CharField(widget=forms.TextInput(
        {"placeholder": "Full Name"}), required=True)
    
    contractor_email = forms.EmailField(widget=forms.TextInput(
        {"placeholder": "Your Email"}), required=True)
    
    contractor_address = forms.CharField(widget=forms.TextInput(
        {"placeholder": "Current Address"}), required=True)
    
    contractor_contact = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "Current Contact Number"}), required=True)
    
    contractor_description = forms.CharField(widget=forms.TextInput(
        {"placeholder": "Description about your work... "}), required=True)
    
    year_of_experience = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "Years Of Experience"}), required=True)
    
    project_ongoing = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "Number of projects currently you are working..."}), required=True)
    
    projects_completed = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "Number of projects completed successfully..."}), required=True)
    
    number_of_successful_clients = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "Number of Successful Clients..."}), required=True)
    
    rating = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "onsite or google rating (out of 5)"}), required=True)
    
    contact_number_of_previous_client = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "Contact Number of Previous Client..."}), required=True)
    
    contractor_Img = forms.ImageField(label="Your Image")

    class Meta(UserCreationForm.Meta):
        model = Users

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_contractor = True
        user.is_staff = True
        user.contractor_name = self.cleaned_data.get('contractor_name')
        user.save()
        contractor = Contractor.objects.create(user=user)
        contractor.contractor_email=self.cleaned_data.get('contractor_email')
        contractor.contractor_address=self.cleaned_data.get('contractor_address')
        contractor.contractor_contact=self.cleaned_data.get('contractor_contact')
        contractor.contractor_description=self.cleaned_data.get('contractor_description')
        
        contractor.year_of_experience = self.cleaned_data.get('year_of_experience')
        contractor.project_ongoing = self.cleaned_data.get('project_ongoing')
        contractor.projects_completed = self.cleaned_data.get('projects_completed')
        contractor.number_of_successful_clients = self.cleaned_data.get('number_of_successful_clients')
        contractor.rating = self.cleaned_data.get('rating')
        contractor.contact_number_of_previous_client = self.cleaned_data.get(
            'contact_number_of_previous_client')
        contractor.contractor_Img = self.cleaned_data.get('contractor_Img')
        contractor.save()
        return user
    
    
class Contact(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
