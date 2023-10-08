from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views import View
from django.contrib.auth.models import User
from .models import frenchise_register_model,frenchise_employee_register_model
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
        r_form = FrenchiseRegistrationForm(data=request.POST)
        # c_form = RolesForm(data=request.POST)
        if r_form.is_valid():
            user = r_form.save()
            user.save()
            # cate = c_form.save(commit=False)
            # cate.user = user
            # cate.save()
            username = r_form.cleaned_data.get('username')
            raw_password = r_form.cleaned_data.get('password')
            # category = c_form.cleaned_data.get('category')
            user = authenticate(username=username, password=raw_password)
            return redirect('profile')
        return render(request, 'frenchise/frenchise_registration.html',  {'r_form': r_form})
        
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
    add = frenchise_employee_register_model.objects.filter(user=request.user)
    return render(request, 'frenchise/frenchise_dashboard.html', {'add': add})



def frenchise_confirmation(request):
    return render(request, 'frenchise/wait_for_confirmation.html')