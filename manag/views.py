from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from manag.models import Contact
from manag.models import Doctor
from manag.models import Patient
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def About(request):
    return render(request,'about.html')

def Add_Contact(request):
      if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject=request.POST.get('subject')
        desc = request.POST.get('desc')
        print(name,email,phone,subject,desc)
        contact = Contact(name=name, email=email, phone=phone, subject=subject,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent!')
      return render(request, 'contact.html')
 



def Add_Doctor(request): 
   
    if request.method == 'POST':
        n = request.POST.get('name')
        m = request.POST.get('mobile')
        sp = request.POST.get('special')

        doctor= Doctor.objects.create(name=n, mobile=m, special=sp)
        doctor.save()   
        messages.success(request, 'Your Message has been sent!')
    return render(request, 'doctor.html')



def Add_Patient(request):
   
    if request.method == 'POST':
        n = request.POST.get('name')
        g = request.POST.get('gender')
        m = request.POST.get('mobile')
        a = request.POST.get('address')
        
        patient= Patient.objects.create(name=n, gender=g, mobile=m, address=a)
        patient.save()   
        messages.success(request, 'Your Message has been sent!')
    return render(request, 'patient.html')



def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        
      
        

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
            messages.success(request, 'Your Message has been sent!')
    return render(request, 'signup.html')


        


def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password1')
        user=authenticate(request, username=username, password1=pass1)
        # if user is  None:
        #     return HttpResponse("Username or Password is incorrect!!!")
        # else:
        #     login(request, user)

        return redirect('index')
        messages.success(request, 'Your Message has been sent!')
    return render(request, 'login.html')
        



def Logout(request):
    logout(request)
    return redirect('login')




