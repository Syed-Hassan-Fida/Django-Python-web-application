from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    
    path('register/',views.register, name='register'),
    path('main/',views.main, name='main'),
    path('customer_register/',views.customer_register.as_view(), name='customer_register'),
    path('employee_register/',views.employee_register.as_view(), name='employee_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('contact_us/', views.contact_us, name='contact_us'),
    # path('', views.register, name="register"),
    # path('signup/', views.signup_view, name="signup"),
    # path('login/', views.login_view, name="login"),
    # path('logout/', views.logout_view, name="logout"),
]
