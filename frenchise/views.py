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
from django.core.mail import send_mail
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
        send_mail(
        "Request for frenchise",
        "Your request for a franchise is under review. Our team will get back to you within 24 hours.",
        "mmaurya7475@gmail.com",
        [raw_email],
        fail_silently=False,
        )
            
        return redirect('home')
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
        
            return redirect('dashboard')
        return render(request, 'frenchise/frenchise_profile.html',  {'a_form': a_form})
        
    else:
        a_form = frenchise_application_form()
        return render(request, 'frenchise/frenchise_apply_form.html', {'a_form': a_form})

 



def profile(request):
    return render(request, 'frenchise/frenchise_profile.html' )



@login_required
def employee_view(request):

    if request.method == 'POST':
        # emp_form = Employee_application_form(data=request.POST)

        # if emp_form.is_valid():
            # Validate the employee ID and email address
        employee_ids = request.POST.get('employee_id')
        emails = request.POST.get('email')
        usernames = request.POST.get('username')
        passwords = request.POST.get('password')
        employee_creation = frenchise_employee_register_model.objects.create(user=request.user, employee_id=employee_ids,email=emails,username=usernames, password=passwords)       
        usernames = usernames +'_emp'
        user = User.objects.create(
            username=  usernames
        
            # role='User',
            # password=passs,
        )
        v = user.set_password(passwords)
        print(v)
        # user.save()
        # print([name,raw_password,raw_city,raw_dob,raw_education,raw_state,raw_number,raw_occupation])
        # user = r_form.save()
        # user.is_active = False
        user.save()
        users = User.objects.get(username=usernames)
            # user.is_active = False
        users.passwo = passwords
        # ProfileFrenchise.objects.create(user=users,DOB=raw_dob,state=raw_state,email=raw_email,city=raw_city,number=raw_number,Occupation=raw_occupation,Education=raw_education)

    #     user = models.ForeignKey(User, on_delete=models.CASCADE)
    # employee_id = models.IntegerField(default=123456)
    # email = models.EmailField(null=False, blank=False, default= 'employee@gmail.com')
    # username = models.CharField(max_length=15,null=False, blank=False, default='Username')
    # password = models.CharField(max_length=50)
   
        print('sjjdgjksgkjbskjbk')
        # user = emp_form.save()
        # user.save()

        print('mansjhisbbbdg')

            # if not validate_employee_id(employee_id):
            #     raise ValidationError('Invalid employee ID.')
            # if not validate_email(email):
            #     raise ValidationError('Invalid email address.')

            # Save the employee application form
            # emp_form.save()

            # Authenticate the user
        # user = authenticate(employee_id=employee_id, email=email,username=username,password=password)
            # login(request, user)

            # Redirect the user to the dashboard
        return redirect('dashboard')

        # If the form is not valid, re-render the form
        return render(request, 'frenchise/employee_dashboard.html', {'emp_form': emp_form})

    else:
        # If the request method is not POST, render the employee application form
        emp_form = Employee_application_form()
        return render(request, 'frenchise/employee_dashboard.html', {'emp_form': emp_form})


    
#dashboard
def dashboard(request):
    e_register = frenchise_employee_register_model.objects.filter(user=request.user)
    f_register = frenchise_register_model.objects.filter(user=request.user)
    return render(request, 'frenchise/frenchise_dashboard.html', {'e_register': e_register, 'f_register':f_register})



def frenchise_confirmation(request):
    return render(request, 'frenchise/wait_for_confirmation.html')

def employee_registration_view(request):
    return render(request, 'frenchise/employee_registration.html')

def employee_dashboard_view(request):
    return render(request, 'frenchise/employee_dashboard.html')

def edit_employee_dashboard_view(request):
    return render(request, 'frenchise/edit_employee_dashboard.html')