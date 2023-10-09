from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views import View
from django.contrib.auth.models import User
from .models import frenchise_register_model,frenchise_employee_register_model,ProfileFrenchise
from .forms import FrenchiseRegistrationForm, frenchise_application_form, Employee_application_form
from django.contrib.auth.decorators import login_required
from fastapi.responses import RedirectResponse, HTMLResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'frenchise/index.html' )

#registration
def frenchise_registration_view(request):
    if request.method == 'POST':
        # r_form = FrenchiseRegistrationForm(data=request.POST)
        # c_form = RolesForm(data=request.POST)
        # if r_form.is_valid():

        # username = r_form.cleaned_data.get('username')
        name = request.POST.get('name')
        # print(name)
        raw_password = request.POST.get('password')
        raw_education = request.POST.get('education')
        raw_occupation = request.POST.get('occupation')
        raw_number = request.POST.get('number')
        raw_state = request.POST.get('state')
        raw_city = request.POST.get('city')
        raw_dob      =  request.POST.get('dateInput')
        raw_email = request.POST.get('email')
        # passs = number+"Nakshtravani@"
        passs = str(raw_password)
        print(passs)
        user = User.objects.create(
            username=raw_number
            # role='User',
            # password=passs,
        )
        v = user.set_password(passs)
        print(v)
        # user.save()
        print([name,raw_password,raw_city,raw_dob,raw_education,raw_state,raw_number,raw_occupation])
        # user = r_form.save()
        user.is_active = False
        user.save()
        users = User.objects.get(username=raw_number)
            # user.is_active = False
        users.passwo = passs
        ProfileFrenchise.objects.create(user=users,DOB=raw_dob,state=raw_state,email=raw_email,city=raw_city,number=raw_number,Occupation=raw_occupation,Education=raw_education)
        # cate = c_form.save(commit=False)
        # users.is_active = False
        # users.save()

        # cate.user = user
        # cate.save()
        

        # category = c_form.cleaned_data.get('category')
        # user = authenticate(username=username, password=raw_password)
        return redirect('profile')
        # return render(request, 'frenchise/frenchise_registration.html',  {'r_form': r_form})
        
    else:
        r_form = FrenchiseRegistrationForm()
        return render(request, 'frenchise/frenchise_registration.html', {'r_form': r_form})





@login_required
def frenchise_application_view(request):
    if request.method == 'POST':
        a_form = frenchise_application_form(request.POST)
        current_user = request.user 
        print("fhjkl")
        print(current_user)
        if a_form.is_valid():
            # print(request.User)
            a_form.instance.user=current_user
            a_form.save()
        
            return redirect('profile')
        return render(request, 'frenchise/frenchise_profile.html',  {'a_form': a_form})
        
    else:
        a_form = frenchise_application_form()
        return render(request, 'frenchise/frenchise_apply_form.html', {'a_form': a_form})

 



def profile(request):
    return render(request, 'frenchise/frenchise_profile.html' )

@login_required
def employee_view(request):
    if request.method == 'POST':
        e_form = Employee_application_form(request.POST)
        current_user = request.user 
        print("fhjkl")
        print(current_user)
        if e_form.is_valid():
            # print(request.User)
            e_form.instance.user=current_user
            e_form.save()
        
            return redirect('profile')
        return render(request, 'frenchise/frenchise_profile.html',  {'e_form': e_form})
        
    else:
        e_form = Employee_application_form()
        return render(request, 'frenchise/employee.html', {'e_form': e_form})
    

def dashboard(request):
    e_register = frenchise_employee_register_model.objects.filter(user=request.user)
    f_register = frenchise_register_model.objects.filter(user=request.user)
    return render(request, 'frenchise/frenchise_dashboard.html', {'e_register': e_register, 'f_register':f_register})



def frenchise_confirmation(request):
    return render(request, 'frenchise/wait_for_confirmation.html')


def employee_dashboard_view(request):
    return render(request, 'frenchise/employee_dashboard.html')

def edit_employee_dashboard_view(request):
    return render(request, 'frenchise/edit_employee_dashboard.html')