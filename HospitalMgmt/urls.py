"""HospitalMgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# username: hospital23
# password: hosmansys@2304

from django.contrib import admin
from django.urls import path
from hospital.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name="home"),
    path('admin_login/', Login, name="login"),
    path('logout/', Logout_admin, name="logout"),

    path('about/', About,name='about'),
    path('contact/', Contact,name='contact'),

# URL's for Doctor's
    path('view_doctor/', View_Doctor,name='view_doctor'),
    path('add_doctor/', Add_Doctor,name='add_doctor'),
    path('delete_doctor(?P<int:pid>)', Delete_doctor,name='delete_doctor'),

# URL's for Patient
    path('add_patient/', Add_patient, name='add_patient'),
    path('view_patient/', View_patient, name='view_patient'),
    path('delete_patient(?P<int:pid>)', Delete_patient, name='delete_patient'),

# URL's for Appointment
    path('add_appointment/', Add_appointment, name='add_appointment',),
    path('view_appointment/', View_appointment, name='view_appointment',),
    path('delete_appointment(?P<int:pid>)', Delete_appointment, name='delete_appointment'),
]
