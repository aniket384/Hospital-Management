from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login


# Home Page Method:

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')


# Login Page Method:

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


# Logout Page Method:

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


# About Page Method:

def About(request):
    return render(request, 'Pages/about.html')


# Contact Page Method:

def Contact(request):
    return render(request, 'Pages/contact.html')


# Doctor's Page(Add, View, and Delete) Method START:-----

def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n, mobile=c, special=sp)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'Doctor/add_doctor.html', d)

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'Doctor/view_doctor.html', d)

def Delete_doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


# Doctor's Page(Add, View, and Delete) Method END:-----

# Patient Page(Add, View,and Delete) Method START:-----
def Add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['mobile']
        a = request.POST['address']
        g = request.POST['gender']
        try:
            Patient.objects.create(name=n, mobile=c, address=a, gender=g)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'Patient/add_patient.html', d)


def View_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()
    d = {'doc': doc}
    return render(request, 'Patient/view_patient.html', d)

def Delete_patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Patient.objects.get(id=pid)
    doctor.delete()
    return redirect('view_patient')

# Patient Page(Add, View,and Delete) Method END:-----

# Appointment Page(Add, View,and Delete) Method START:-----

def Add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t)
            error = "no"
        except:
            error = "yes"
    d = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'Appointment/add_appointment.html', d)


def View_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    d = {'appoint': appoint}
    return render(request, 'Appointment/view_appointment.html', d)

def Delete_appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.get(id=pid)
    appoint.delete()
    return redirect('view_appointment')

# Appointment Page(Add, View,and Delete) Method END:-----
