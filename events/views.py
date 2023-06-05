from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from stu_cou_reg.models import StudentData,CourseData,RegisteredData


def index(request):
    cou = CourseData.objects.all().values()
    return render(request,'index.html',{ 'cou' : cou })

def student_login(request):
    return render(request,'std_login.html')

def student_signup(request):
    return render(request,'std_signup.html')

def admin_login(request):
    return render(request,'admin_login.html')
 


