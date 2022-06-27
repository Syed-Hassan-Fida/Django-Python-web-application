from django.urls import path, re_path
# from django.conf.urls import url
from django.urls import include, re_path
from . import views

app_name = 'tycoonConstruction'

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('hireVendor/', views.Vendor_details, name='hireVendor'),
    path('vendorAdmin/', views.vendor_Admin, name='vendorAdmin'),
    path('contractorAdmin/', views.contractor_Admin, name='contractorAdmin'),
    path('hireContractor/', views.hire_contractor, name='hireContractor'),
    # Bidding route
    path('hireContractor/bidContractor/<int:id>', views.bidContractorr, name='bidContractorr'),
    path('hireVendor/bidVendor/<int:id>',
         views.bid_Vendor, name='bid_Vendor'),
    # cost calculation
    path('costEstimation/', views.cost_estimation, name='costEstimation'),
    path('brickwall/', views.brickwall, name='brickwall'),
    path('walldeduction/', views.walldeduction, name='walldeduction'),
    path('labourcost/', views.labourcost, name='labourcost'),
    path('pillarandbeam/', views.pillarandbeam, name='pillarandbeam'),
    # vendor_details
     path('vendor_details/', views.vendor_admin_details,
          name='vendor_details'),
     # VtoC request
     path('vtoc_request/<int:id>', views.vtoc_request, name='vtoc_request'),
     # contractor_details
     path('contractor_details/', views.contractor_details,
          name='contractor_details'),
     # delete client bit to vendor
     path('delete_v_bid/<int:id>', views.delete_v_bid, name='delete_v_bid'),
     # delete client bit to contractor
     path('contractorAdmin/contractorAdmin/<int:id>', views.delete_c_bid, name='delete_c_bid'),
     #     vtoc details
     path('vtoc_details/', views.vtoc_details, name='vtoc_details'),
     # delete vtoc request 
     path('vtoc_details/vtoc_details/<int:id>',views.delete_vtoc_request, name='delete_vtoc_request'),
     # Accept Client Request From Contractor
     path('contractorAdmin/accept_client_request/<int:id>', views.accept_client_request, name='accept_client_request'),
     # Accept Vendor Request From Contractor
     path('vtoc_details/accept_vender_request/<int:id>', views.accept_vender_request, name='accept_vender_request'),
      # Accept Client Request From Vendor
     path('vendorAdmin/vtoclient_accept/<int:id>',views.vtoclient_accept,name='vtoclient_accept'),
      # Delete Client From Vendor
     path('vendorAdmin/vendorAdmin/<int:id>',views.vtoclient_delete,name='vtoclient_delete'),
     # accpeted projects v to cli 
     path('projects_vtocli/', views.projects_vtocli, name='projects_vtocli'),
     
]