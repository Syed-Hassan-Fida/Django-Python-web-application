from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import CreateView
from .form import VendorSignUpForm, ContractorSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .form import Contact
from .models import Users, Contact_us

# //////////////// 
def contact_us(request):
    if request.method == "POST":
        fm = Contact(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ph = fm.cleaned_data['phone']
            email = fm.cleaned_data['email']
            mesg = fm.cleaned_data['message']
            reg = Contact_us(name=nm, phone=ph, email=email, message=mesg)
            reg.save()
            fm = Contact()
    else:
        fm = Contact()
    return render(request, 'contact_us.html', {'form': fm})
    

def register(request):
    return render(request, 'register.html')

def main(request):
    return render(request, 'index.html')


class customer_register(CreateView):
    model = Users
    form_class = VendorSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

# Venddor registration
class employee_register(CreateView): 
    model = Users
    form_class = ContractorSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                # return redirect('index.html')
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    if user.is_vendor:
                        return redirect('tycoonConstruction:vendorAdmin')
                    elif user.is_contractor:
                        return redirect('tycoonConstruction:contractorAdmin')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html', context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('tycoonConstruction:home')









# # Create your views here.

# def register(request):
#     return render(request, 'accounts/registration.html')

# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('tycoonConstruction:home')
#     else:
#         form = UserCreationForm()    
    
#     return render(request, 'accounts/signup.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect('tycoonConstruction:home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})


# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('tycoonConstruction:home')
