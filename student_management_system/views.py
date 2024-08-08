from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from . models import *


# Create your views here.
def index(request):
    return render(request, 'index.html') 

def studentlogin(request):
    return render(request, 'studentlogin.html') 

def coursedetails(request):
    return render(request, 'coursedetails.html') 

def studentreg(request):
    if request.method=='POST':
        sname=request.POST.get('sname')
        semail=request.POST.get('semail')
        snumber=request.POST.get('snumber')
        sage=request.POST.get('sage')
        senrollment_date=request.POST.get('senrollment_date')
        scourse=request.POST.get('scourse')

        sdetails=studentdetail(sname=sname,semail=semail,snumber=snumber,sage=sage,senrollment_date=senrollment_date,scourse=scourse)
        sdetails.save()
        log = {
            'sname': sname,
            'semail': semail,
            'snumber': snumber,
            'sage': sage,
            'senrollment_date': senrollment_date,
            'scourse': scourse
        }
        return render(request,"studentlogin.html",log)
    return render(request,'index.html')

def coursedetails(request):
    courses = studentdetail.objects.values_list('scourse', flat=True).distinct()
    return render(request, 'coursedetails.html', {'courses': courses})

def coursestudent(request,coursename):
    students = studentdetail.objects.filter(scourse=coursename)
    return render(request, 'coursestudent.html', {'students':students,'coursename':coursename})