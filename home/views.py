from django.shortcuts import render

# Create your views here.


from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout



def home(request):
    return render(request, 'home/base.html',
                  {'home': home})

def about(request):
    return render(request, 'home/about.html',
                  {'about': about})


def mentor(request):
    return render(request, 'home/mentor.html',
                  {'mentor': mentor})

def index(request):
    return render(request, 'home/index.html',
                  {'index': index})

def empindex(request):
    return render(request, 'home/empindex.html',
                  {'empindex': empindex})

def emphome(request):
    return render(request, 'home/emphome.html',
                  {'emphome': emphome})

def mentorhome(request):
    return render(request, 'home/mentorhome.html',
                  {'mentorhome': mentorhome})

def markattendance(request):
    return render(request, 'home/markattendance.html',
                  {'markattendance': markattendance})

def studentsreports(request):
    return render(request, 'home/studentsreports.html',
                  {'studentsreports': studentsreports})

def createappointments(request):
    return render(request, 'home/createappointments.html',
                  {'createappointments': createappointments})

def empmarkattendance(request):
    return render(request, 'home/empmarkattendance.html',
                  {'empmarkattendance': empmarkattendance})

def empstudentsreports(request):
    return render(request, 'home/empstudentsreports.html',
                  {'empstudentsreports': empstudentsreports})

def empcreateappointments(request):
    return render(request, 'home/empcreateappointments.html',
                  {'empcreateappointments': empcreateappointments})

def mentorlist(request):
    return render(request, 'home/mentorlist.html',
                  {'mentorlist': mentorlist})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'home/base.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return render(request, 'home/emphome.html')
            else:
                login(request, user)
                return render(request, 'home/mentorhome.html')
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})
    return render(request, 'home/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/login.html')
    context = {
        "form": form,
    }
    return render(request, 'home/register.html', context)

def password_reset(request):
    return render(request, 'home/password_reset.html',
    {'home': password_reset})


def password_reset_confirm(request):
    return render(request, 'home/password_reset_confirm.html',
    {'home': password_reset_confirm})

def password_reset_email(request):
    return render(request, 'home/password_reset_email.html',
    {'home': password_reset_email})

def password_reset_complete(request):
    return render(request, 'home/password_reset_complete.html',
    {'home': password_reset_complete})

def Student_list(request):
    students = Student.objects.filter(start_date__lte=timezone.now())
    return render(request, 'home/studentlist.html',
    {'home': students})


def studentedit(request):
   student = get_object_or_404(Student)
   if request.method == "POST":
       form = StudentForm(request.POST, instance=student)
       if form.is_valid():
           student = form.save()
           # stock.customer = stock.id
           student.updated_date = timezone.now()
           student.save()
           students = Student.objects.filter(start_date__lte=timezone.now())
           return render(request, 'home/studentlist.html', {'student': students})
   else:
       # print("else")
       form = StudentForm(instance=student)
   return render(request, 'home/studentedit.html', {'form': form})

def studentadd(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.start_date = timezone.now()
            student.save()
            students = Student.objects.filter(start_date__lte=timezone.now())
            return render(request, 'home/studentlist.html',
                          {'student': students})
    else:
        form = StudentForm()
        # print("Else")
    return render(request, 'home/studentadd.html', {'form': form})



def studentsarchive(request):
    student = get_object_or_404(Student)
    if request.method =="POST":
       form = StudentForm(request.POST, instance = student)
       print("one")
       if form.is_valid():
           print("2")
           student= form.save()
           print("3")
           Stud_id = form.cleaned_data['Student ID']
           print("4")
           student_arch= Student.object.filter(Student_id = Stud_id)
           print("5")
           student_arch.delete()
           students = StudentForm(instance=student)
           return render(request, 'home/studentlist.html', {'student': students})

    else:
           print("else")
     #  form = StudentForm(instance=student)
      # return render(request, 'home/studentsarchive.html', {'form': form})
