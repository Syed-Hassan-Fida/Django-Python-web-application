from django.contrib import admin
from .models import Users, Vendor, Contractor, Contact_us


admin.site.register(Users)
admin.site.register(Vendor)
admin.site.register(Contractor)
admin.site.register(Contact_us)
list_dilplay = ('name', 'phone''email', 'message')
