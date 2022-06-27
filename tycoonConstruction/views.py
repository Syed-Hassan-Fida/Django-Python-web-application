from datetime import datetime
from multiprocessing import context
from django.contrib import messages
import re
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from pytz import timezone
from accounts.models import Contractor, Users
from tycoonConstruction.models import bidContractor, bidVendor, Accept_request, Accept_vendor_request, Vendor_accept
from datetime import datetime
import smtplib
from accounts.models import Vendor, Contractor
from .form import CostForm, Deduction, LabourCost, PillarCollumn, RccBeam, RccSlap, Vtoc_req
from .models import Estimation, VtoC_req
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'tycoonConstruction/index.html')


def services(request):
    return render(request, 'tycoonConstruction/services.html')


def hire_contractor(request):
    con = Contractor.objects.all().order_by('-pk')
    # count = len(con)+1
    # print(f"lenght is ---------------> {count}")
    context = {
        'con': con,
    }
    print(context)
    return render(request, 'tycoonConstruction/hire_contractor.html', context)


def hire_vendor(request):

    return render(request, 'tycoonConstruction/hire_vendor.html')


@login_required(login_url='/accounts/login')
def vendor_Admin(request):
    proj = bidVendor.objects.all()
    return render(request, 'tycoonConstruction/vendorAdmin.html', {'proj': proj})


@login_required(login_url='/accounts/login')
def contractor_Admin(request):
    proj = bidContractor.objects.all()
    return render(request, 'tycoonConstruction/contractorAdmin.html', {'proj': proj})


def bidContractorr(request, id):
    id = id
    specific_user = Contractor.objects.get(pk=id)
    con_email = specific_user.contractor_email
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile_no = request.POST['mobile_no']
        email = request.POST['email']
        project_address = request.POST['project_address']
        project_budget = request.POST['project_budget']
        desc = request.POST.get('desc')
        mini_vendors = request.POST['mini_vendors']
        meeting_date = request.POST['meeting_date']
        en = bidContractor(first_name=first_name, last_name=last_name, mobile_no=mobile_no,
                           email=email, project_address=project_address, desc=desc,
                           meeting_date=meeting_date, project_budget=project_budget, mini_vendors=mini_vendors, contractor=specific_user)
        en.save()
        # Now Sending email process start
        gmail_user = "tycoonconstruction32@gmail.com"
        gmail_pwd = "alpha@12345"
        TO = con_email
        SUBJECT = "NEW CUSTOMER!"
        TEXT = "Hey Contarctor, Someone is looking for you..."
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_user,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])
        server.sendmail(gmail_user, [TO], BODY)
        print(f'Email has been send successfully!')
        return redirect('/hireContractor')
    else:
        return render(request, 'tycoonConstruction/bidContractor.html')


@login_required(login_url='/accounts/login')
def contractor_details(request):
    contractor = Contractor.objects.all().order_by('-pk')
    return render(request, 'tycoonConstruction/contractor_details.html', {'contractor': contractor})


@login_required(login_url='/accounts/login')
def clientDetails(request):
    user = bidContractor.objects.all()
    context = {
        'user': user
    }
    print(user)
    return render(request, 'tycoonConstruction/clientDetails.html', {'user': user})


#  vendor Views and Functions
def Vendor_details(request):
    vendor = Vendor.objects.all().order_by('-pk')
    return render(request, 'tycoonConstruction/hire_vendor.html', {'vendor': vendor})


@login_required(login_url='/accounts/login')
def vendor_admin_details(request):
    vendor = Vendor.objects.all().order_by('-pk')
    return render(request, 'tycoonConstruction/vendor_details.html', {'vendor': vendor})

#  vendor to contrator request


@login_required(login_url='/accounts/login')
def vtoc_request(request, id):
    specific_user = Contractor.objects.get(pk=id)
    submitbutton = request.POST.get("submit")
    if request.method == "POST":
        form = Vtoc_req(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            v_email=form.cleaned_data.get("v_email")
            year_of_experience = form.cleaned_data.get("year_of_experience")
            projects_done = form.cleaned_data.get("projects_done")
            rating = form.cleaned_data.get("rating")
            description = form.cleaned_data.get("description")
            image = form.cleaned_data.get("image")
            obj = VtoC_req.objects.create(
                name=name,v_email=v_email,
                year_of_experience=year_of_experience,
                projects_done=projects_done, rating=rating, description=description,
                image=image, contractor=specific_user
            )
            messages.success(
                request, "Your request has been Sended Successfuly...")
            obj.save()
    else:
        form = Vtoc_req()
    context = {
        'form': form, 'submitbutton': submitbutton
    }
    return render(request, 'tycoonConstruction/vtoc_request.html', context)

#  vtoc details


@login_required(login_url='/accounts/login')
def vtoc_details(request):
    requests = VtoC_req.objects.all()
    return render(request, 'tycoonConstruction/vtoc_details.html', {'requests': requests})


def bid_Vendor(request, id):
    id = id
    specific_user = Vendor.objects.get(pk=id)
    con_email = specific_user.vendor_email
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile_no = request.POST['mobile_no']
        email = request.POST['email']
        project_address = request.POST['project_address']
        project_budget = request.POST['projectbudget']
        desc = request.POST.get('desc')

        meeting_date = request.POST['meeting_date']
        en = bidVendor(first_name=first_name, last_name=last_name, mobile_no=mobile_no,
                       email=email, project_address=project_address, desc=desc, meeting_date=meeting_date,
                       projectbudget=project_budget, vendor=specific_user)
        en.save()
        # Now Sending email process start
        gmail_user = "tycoonconstruction32@gmail.com"
        gmail_pwd = "alpha@12345"
        TO = con_email
        SUBJECT = "NEW CUSTOMER!"
        TEXT = "Hey Vendor, Someone is looking for you..."
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_user,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])
        server.sendmail(gmail_user, [TO], BODY)
        print(f'Email has been send successfully!')
        return redirect('/hireVendor')
    else:
        return render(request, 'tycoonConstruction/bidVendor.html')

# Accept Client Request from Contractor


@login_required(login_url='/accounts/login')
def accept_client_request(request, id):
    id = id
    specific_user = bidContractor.objects.get(pk=id)
    con_email = specific_user.email
    if request.method == "POST":
        msg = request.POST['msg']
        bool = request.POST['bool']
        
        obj = Accept_request(msg=msg, bool=bool, projects=specific_user)
        obj.save()
        # Now Sending email process start
        gmail_user = "tycoonconstruction32@gmail.com"
        gmail_pwd = "alpha@12345"
        TO = con_email
        SUBJECT = "Acceptation From Contractor To Client!"
        TEXT = msg
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_user,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])
        server.sendmail(gmail_user, [TO], BODY)
        print(f'Email has been send successfully!')
        # return render(request, 'tycoonConstruction/contractorAdmin.html')
        # return HttpResponseRedirect('/')
        return redirect('/contractorAdmin') 
    else:
        return render(request, 'tycoonConstruction/accept_client_request.html')

# Accept Vendor Request from Contractor


@login_required(login_url='/accounts/login')
def accept_vender_request(request,id):
    id = id
    specific_user = VtoC_req.objects.get(pk=id)
    con_email = specific_user.v_email
    vendr = bidVendor.objects.all()
    context = {
        'vendr': vendr
    }
    print(vendr)
    if request.method=="POST":
        mesg = request.POST.get('mesg')
        bool = request.POST.get('bool')
        en = Accept_vendor_request(
            mesg=mesg, bool=bool, vtoc_req=specific_user)
        en.save()
        # Now Sending email process start
        gmail_user = "tycoonconstruction32@gmail.com"
        gmail_pwd = "alpha@12345"
        TO = con_email
        SUBJECT = "Acceptation From Contractor To Vendor!"
        TEXT = mesg
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_user,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])
        server.sendmail(gmail_user, [TO], BODY)
        print(f'Email has been send successfully!')
        return redirect('/contractorAdmin') 
    else:
        return render(request, 'tycoonConstruction/accept_vender_request.html')


# Accept Client Request from Vendor
@login_required(login_url='/accounts/login')
def vtoclient_accept(request,id):
    vn = Vendor_accept.objects.all()
    context={
        'vn':vn
    }
    id = id
    specific_user = bidVendor.objects.get(pk=id)
    con_email = specific_user.email
    if request.method == "POST":
        v_mesg = request.POST['v_mesg']
        bool = request.POST['bool']
        obj = Vendor_accept(v_mesg=v_mesg, bool=bool, projects=specific_user)
        obj.save()
        # Now Sending email process start
        gmail_user = "tycoonconstruction32@gmail.com"
        gmail_pwd = "alpha@12345"
        TO = con_email
        SUBJECT = "Acceptation From Vendor To Client!"
        TEXT = v_mesg
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_user,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])
        server.sendmail(gmail_user, [TO], BODY)
        print(f'Email has been send successfully!')
        # return render(request, 'tycoonConstruction/contractorAdmin.html')
        # return HttpResponseRedirect('/')
        return redirect('/vendorAdmin') 
    else:
        return render(request, 'tycoonConstruction/vtoclient_accept.html', context)

 # Delete Client From Vendor
@login_required(login_url='/accounts/login')
def vtoclient_delete(request,id):
    if request.method=="POST":
        pi=bidVendor.objects.get(pk=id)
        pi.delete()
        return redirect('/vendorAdmin')
    else:
        return render(request, 'tycoonConstruction/contractorAdmin.html')



#  delete function
@login_required(login_url='/accounts/login')
def delete_v_bid(request, id):
    bidVendor.objects.get(pk=id).delete()
    return render(request, 'tycoonConstruction/vendorAdmin.html')


@login_required(login_url='/accounts/login')
def delete_c_bid(request, id):
    if request.method=="POST":
        pi=bidContractor.objects.get(pk=id)
        pi.delete()
        return redirect('/contractorAdmin')
    else:
        return render(request, 'tycoonConstruction/contractorAdmin.html')


@login_required(login_url='/accounts/login')
def delete_vtoc_request(request,id):
    if request.method=="POST":
        pi=VtoC_req.objects.get(pk=id)
        pi.delete()
        return redirect('/contractorAdmin')
    else:
        return render(request, 'tycoonConstruction/contractorAdmin.html')


@login_required(login_url='/accounts/login')
def delete_vtoc_req(request, id):
    VtoC_req.objects.get(pk=id).delete()
    return render(request, 'tycoonConstruction/vtoc_details.html')

def projects_vtocli(request):
    v_proj = Vendor_accept.objects.filter(bool=True)
    c_proj = Accept_request.objects.filter(bool=True)
    vtoc_request = Accept_vendor_request.objects.filter(bool=True)
    print('vtoc_request ', vtoc_request)
    return render(request, 'tycoonConstruction/projects_vtocli.html', 
                  {'v_proj': v_proj, 'c_proj': c_proj, 'vtoc_request': vtoc_request})



# cost estimation functions


def cost_estimation(request):
    if request.method == 'GET':
        cost = Vendor.objects.all()
    return render(request, 'tycoonConstruction/cost_Estimation.html', {'cost': cost})


def brickwall(request):
    submitbutton = request.POST.get("submit")

    cost = Estimation.objects.all()
    for i in cost:
        brickCost = i.brickCost
        cementCost = i.cementCost
        sandCost = i.sandCost

    cost_of_brick = brickCost
    cement_bag = cementCost
    sand_price_m_cube = sandCost

    meter = 3.281
    inch = 0.0254
    length = 0.00
    width = 0.00
    height = 0.00
    no_of_walls = 0.00
    brick_used = 0
    total_POB = 0
    cement_used = 0
    cement_price = 0
    sand_used = 0
    sand_price = 0
    total_meter_wall=0
    bool=False
    context = {}

    form = CostForm(request.POST or None)
    if form.is_valid():
        length = form.cleaned_data.get("length")
        width = form.cleaned_data.get("width")
        height = form.cleaned_data.get("height")
        no_of_walls = form.cleaned_data.get("no_of_walls")
        bool=True
    
    
    total_meter_wall = (length/meter)*(height/meter)*(width*inch)*no_of_walls

    # brick cost
    brick_used = total_meter_wall*500
    total_POB = brick_used*cost_of_brick

    # cement cost
    cement_used = total_meter_wall*2.15
    cement_price = cement_used*cement_bag

    # sand cost
    sand_used = total_meter_wall*0.225
    sand_price = sand_used*sand_price_m_cube

    total_price = total_POB + cement_price + sand_price
    context = {
        'form': form, 'length': length, 'width': width, 'height': height,
        'no_of_walls': no_of_walls, 'submitbutton': submitbutton, 'total_meter_wall': round(total_meter_wall, 2),
        'cement_used': round(cement_used, 0), 'cement_price': round(cement_price, 0),
        'sand_used': round(sand_used, 2), 'sand_price': round(sand_price, 0),
        'total_POB': round(total_POB, 0), 'brick_used': round(brick_used, 0), 'bool': bool,
        'total_price': round(total_price, 0)
    }

    return render(request, 'tycoonConstruction/brickwall.html', context)
    


def walldeduction(request):
    submitbutton = request.POST.get("submit")
    cost = Estimation.objects.all()
    for i in cost:
        brickCost = i.brickCost
        cementCost = i.cementCost
        sandCost = i.sandCost

    cost_of_brick = brickCost
    cement_bag = cementCost
    sand_price_m_cube = sandCost

    meter = 3.281
    inch = 0.0254
    length = 0.00
    width = 0.00
    height = 0.00
    no_of_walls = 0.00
    total_wall = 0.00
    deduction = 0.00
    brick_used = 0
    total_POB = 0
    cement_used = 0
    cement_price = 0
    sand_used = 0
    sand_price = 0

    context1 = {}

    form1 = Deduction(request.POST or None)
    if form1.is_valid():
        length = form1.cleaned_data.get("length")
        width = form1.cleaned_data.get("width")
        height = form1.cleaned_data.get("height")
        no_of_walls = form1.cleaned_data.get("no_of_walls")
        total_wall = form1.cleaned_data.get("total_meter_wall")

    total_meter_wall = (length/meter)*(height/meter)*(width*inch)*no_of_walls
    deduction = total_wall - total_meter_wall

    # brick cost
    brick_used = deduction*500
    total_POB = brick_used*cost_of_brick

    # cement cost
    cement_used = deduction*2.15
    cement_price = cement_used*cement_bag

    # sand cost
    sand_used = deduction*0.225
    sand_price = sand_used*sand_price_m_cube

    context1 = {
        'form': form1, 'length': length, 'width': width, 'height': height, 'deduction': round(deduction, 2),
        'no_of_walls': no_of_walls, 'submitbutton': submitbutton,
        'total_meter_wall': round(total_meter_wall, 2), 'brick_used': round(brick_used, 0), 'total_POB': round(total_POB, 0),
        'total_wall': total_wall, 'cement_used': round(cement_used, 0), 'cement_price': round(cement_price, 0),
        'sand_used': round(sand_used, 2), 'sand_price': round(sand_price, 0),
    }

    return render(request, 'tycoonConstruction/deduction.html', context1)


def labourcost(request):
    submitbutton = request.POST.get("submit")
    cost = Estimation.objects.all()
    for i in cost:
        labourCost = i.labourCost

    labour_price_1sqft = labourCost

    meter = 3.281
    length = 0.00
    width = 0.00
    total_area = 0.00
    sqft = 0.00
    labour_cost = 0.00
    total_person = 0
    no_days = 0
    avg_work = 8
    value = 0
    context1 = {}

    form1 = LabourCost(request.POST or None)
    if form1.is_valid():
        length = form1.cleaned_data.get("length")
        width = form1.cleaned_data.get("width")
        no_days = form1.cleaned_data.get("no_days")

    # labour cost formula
    total_area = (length/meter)*(width/meter)
    sqft = total_area*10.7634
    labour_cost = sqft*labour_price_1sqft
    # man power
    int_sqft = int(sqft)
    value = (int_sqft/avg_work)
    if no_days > 0:
        total_person = (value/no_days)

    context1 = {
        'form': form1, 'total_area': total_area, 'total_area_sqft': round(sqft, 1), 'labour_cost': round(labour_cost, 0),
        'submitbutton': submitbutton, 'length': length, 'width': width, 'total_person': round(total_person, 0),
        'no_days': no_days
    }
    return render(request, 'tycoonConstruction/labourcost.html', context1)


def pillarandbeam(request):
    submitbutton = request.POST.get("submit")
    cost = Estimation.objects.all()
    for i in cost:
        steelCost = i.steelCost

    cost_of_steel = steelCost

    meter = 3.281
    inch = 0.0254
    c_length = 0.00
    c_width = 0.00
    c_height = 0.00
    c_no_of_walls = 0.00
    b_length = 0.00
    b_width = 0.00
    b_height = 0.00
    b_no_of_walls = 0.00
    s_length = 0.00
    s_width = 0.00
    s_height = 0.00
    s_no_of_walls = 0.00
    volume_of_concrete = 0.01
    steel_density = 7850  # kg/meter cube

    form1 = PillarCollumn(request.POST or None)
    if form1.is_valid():
        c_length = form1.cleaned_data.get("c_length")
        c_width = form1.cleaned_data.get("c_width")
        c_height = form1.cleaned_data.get("c_height")
        c_no_of_walls = form1.cleaned_data.get("c_no_of_walls")

    total_column = (c_length*inch)*(c_width*inch) * \
        (c_height/meter)*c_no_of_walls

    form2 = RccBeam(request.POST or None)
    if form2.is_valid():
        b_length = form2.cleaned_data.get("b_length")
        b_width = form2.cleaned_data.get("b_width")
        b_height = form2.cleaned_data.get("b_height")
        b_no_of_walls = form2.cleaned_data.get("b_no_of_walls")

    total_beam = (b_length/meter)*(b_height*inch)*(b_width*inch)*b_no_of_walls

    form3 = RccSlap(request.POST or None)
    if form3.is_valid():
        s_length = form3.cleaned_data.get("s_length")
        s_width = form3.cleaned_data.get("s_width")
        s_height = form3.cleaned_data.get("s_height")
        s_no_of_walls = form3.cleaned_data.get("s_no_of_walls")

    # Rcc calculation logic
    totalslap = (s_length/meter)*(s_width/meter)*(s_height*inch)*s_no_of_walls

    total_Rcc = total_column+total_beam+totalslap

    total_steel = (volume_of_concrete*total_Rcc)*steel_density
    t_price_of_steel = total_steel*cost_of_steel

    context = {
        'submitbutton': submitbutton, 'form1': form1, 'total_column': round(total_column, 2),
        'total_beam': round(total_beam, 2), 'form2': form2,
        'form3': form3, 'total_steel': round(total_steel, 2), 't_price_of_steel': round(t_price_of_steel, 2),
        'total_Rcc': round(total_Rcc, 2),
        'totalslap': round(totalslap, 2),
    }
    return render(request, 'tycoonConstruction/pillarandbeam.html', context)
