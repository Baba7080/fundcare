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
from django.shortcuts import get_object_or_404
from companystaff.models import *
from datetime import datetime
# Create your views here.
# import matplotlib.pyplot as plt
from io import BytesIO
import base64
def index(request):
    return render(request, 'frenchise/index.html' )

# Frenchise Registration
def frenchise_registration_view(request):
    if request.method == 'POST':

        name = request.POST.get('name')
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
        ProfileFrenchise.objects.create(user=users,DOB=raw_dob,state=raw_state,email=raw_email,city=raw_city,number=raw_number,Occupation=raw_occupation,Education=raw_education,Role="Frenchise")
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

#About
def about_view(request):
    return render(request, 'frenchise/about.html' )

#Services 
def Services_view(request):
    return render(request, 'frenchise/services.html' )

#Blog 
def blog_view(request):
    return render(request, 'frenchise/blog.html' )

#Blog Details
def blog_details_view(request):
    return render(request, 'frenchise/blog_details.html' )

#Contact Us
def contact_view(request):
    return render(request, 'frenchise/contact.html' )




#
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
        name = request.POST.get('name')
        usernames = request.POST.get('username')
        usernames = usernames+"_emp"
        passwords = request.POST.get('password')
        employee_creation = frenchise_employee_register_model.objects.create(user=request.user,name=name, employee_id=employee_ids,email=emails,username=usernames, password=passwords)       
        # usernames = usernames +'_emp'
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
    

#frenchise status True or False

def check_active_frenchise(request):
    if request.method == 'POST':
        active_user = request.POST.get('activeuser')
        if active_user:
            user = User.objects.get(pk=active_user)
            user.is_active = True
            user.save()
        # if request.POST.get('activeuser'):
        #     allUser = User.objects.all()
        #     data = User()
        #  
        #     data.is_active = request.POST.get('activeuser')
        #     data.save()
            
            return render(request,'frenchise/admin_dashboard.html')
    else:
        
        return render(request,'frenchise/admin_dashboard.html')
            
@login_required
def all_frenchise_employe_view(request,frenchid):
    loginUser = request.user
    if loginUser.is_superuser:
        user = get_object_or_404(User, id=frenchid)
        
        # You can directly access the username using user.username
        usernm = user.username
        print(usernm)
        # Query the 'frenchise_employee_register_model' model using the retrieved username
        e_data = frenchise_employee_register_model.objects.filter(user=user)
        all_data = []
        for data in e_data:
            u = data.user
            usernames = data.username
            userdataemp = User.objects.filter(username=usernames)
            # print
            for i in userdataemp:
                usrnme = i.id
            loandata = Loan.objects.filter(user=usrnme)
            count_loan = loandata.count()
            print(count_loan)

            insurance_data = Insurance.objects.filter(user=usrnme)
            count_insurance = insurance_data.count()

            total_sales = count_loan + count_insurance

            data_dict = {
                'id': data.id,
                'employee_id':data.employee_id,
                'username': data.username,
                'email': data.email,
                'total':total_sales,
                'loan':count_loan,
                'insurance':count_insurance
            }
            all_data.append(data_dict)
        return render(request, 'frenchise/all_frenchise_employee_dashboard.html', {'e_data': all_data})

def employee_data_chart(request):
    # Sample employee data (replace with your actual data)
    employees = ['Employee 1', 'Employee 2', 'Employee 3']
    loan_counts = [5, 8, 3]
    insurance_counts = [2, 6, 1]

    # Create a bar chart
    plt.figure(figsize=(8, 4))
    plt.bar(employees, loan_counts, label='Loans')
    plt.bar(employees, insurance_counts, bottom=loan_counts, label='Insurance')

    plt.xlabel('Employees')
    plt.ylabel('Count')
    plt.title('Loan and Insurance Data for Employees')
    plt.legend()

    # Save the chart to a BytesIO object
    chart_buffer = BytesIO()
    plt.savefig(chart_buffer, format='png')
    chart_buffer.seek(0)
    chart_data = base64.b64encode(chart_buffer.read()).decode()
    plt.close()

    context = {
        'chart_data': chart_data,
    }

    return render(request, 'your_template.html', context)

#dashboard
@login_required
def dashboard(request):
    loginUser = request.user
    n = loginUser.username
    words = n.split()
    print(words)
    check = True
    print(len(n))
    if len(n) > 4:
        checkforemp  = n[-4:]

        if checkforemp == '_emp':
            check = False

        
    # profiledata = ProfileFrenchise.objects.get(user=loginUser)
    print(check)
    if loginUser.is_superuser:
        allUser = User.objects.all()
        users_without_emp = User.objects.exclude(username__endswith='_emp')
        return render(request,'frenchise/admin_dashboard.html',{'usersWithout':users_without_emp})
        # print(users_without_emp)
        # for i in users_without_emp:
        #     print(i)
    if check:
        f_register = frenchise_register_model.objects.filter(user=request.user)
        e_register = frenchise_employee_register_model.objects.filter(user=request.user)

        return render(request, 'frenchise/frenchise_dashboard.html', {'e_register':e_register,'f_register':f_register})
    else:
        e_register = frenchise_employee_register_model.objects.filter(username=n)
        return render(request, 'frenchise/employesales.html', {'e_register': e_register})
@login_required
def editfrenchise(request,frenchid):
    users = request.user
    if request.method == 'POST':
        status = request.POST.get('status')
        name = request.POST.get('name')
        address = request.POST.get('address')
        Occupation = request.POST.get('Occupation')
        education = request.POST.get('education')
        number = request.POST.get('number')
        states = request.POST.get('state')
        citys = request.POST.get('city') 
        dateob = request.POST.get('dob')
        coded = request.POST.get('code')
        profileid = request.POST.get('profileid')
        userid = request.POST.get('userdataid')
        date_string = "Oct. 3, 2023"

        # Parse the date string to a datetime object
        date_obj = datetime.strptime(date_string, "%b. %d, %Y")
        print(status)
        if status == 'active':
            status = True
        else:
            status = False
        print(status)
        
        # Format the datetime object to the desired format
        formatted_date = date_obj.strftime("%Y-%m-%d")
        update = ProfileFrenchise.objects.filter(id=profileid).update(frenchise_name=name,Code=coded, DOB=formatted_date,Address_Type=address,Occupation=Occupation,Education=education,number=number,city=citys,state=states)
        updates = User.objects.filter(id=userid).update(is_active=status)
        getIduser = User.objects.get(id=userid)
        user = get_object_or_404(User, id=userid)
        # try:
        getIduser = User.objects.get(id=userid)
        getidProfile = ProfileFrenchise.objects.get(user=getIduser)
        return render(request,'frenchise/editfrenchise.html',{'userdata':getIduser,'profileDta':getidProfile})
        # print(status)
    if users.is_superuser:
        
        getIduser = User.objects.get(id=frenchid)
        user = get_object_or_404(User, id=frenchid)
        try:
            getIduser = User.objects.get(id=frenchid)
            getidProfile = ProfileFrenchise.objects.get(user=getIduser)
            # Now you can access the ProfileFrenchise data associated with the specific user
            print(getidProfile)
        except User.DoesNotExist:
            # Handle the case where the User with the given frenchid doesn't exist
            getIduser = None
            getidProfile = None
            return HttpResponse("user not exist")
        except ProfileFrenchise.DoesNotExist:
            # Handle the case where the ProfileFrenchise for the User doesn't exist
            getidProfile = None
            return HttpResponse("Profile not exist")

        if getidProfile:
            print(getidProfile)
            print(getidProfile)
            return render(request,'frenchise/editfrenchise.html',{'userdata':getIduser,'profileDta':getidProfile})

            # The ProfileFrenchise object exists and can be used here.
        else:
            return HttpResponse("else")



def apply_loan_view(request):
    return render(request, 'frenchise/apply_loan.html')

def frenchise_confirmation(request):
    return render(request, 'frenchise/wait_for_confirmation.html')

def employee_registration_view(request):
    return render(request, 'frenchise/employee.html')

def employee_dashboard_view(request):
    return render(request, 'frenchise/employee_dashboard.html')


@login_required
def edit_employee_dashboard_view(request, empid):
    loginUser = request.user.username
    # getEmployee = frenchise_employee_register_model.objects.filter(id=empid)
    if request.method == 'POST':
        print("inpost")
        emails = request.POST.get('email')
        employeeuiid = request.POST.get('employeId')
        empIds = request.POST.get('empIds')
        print(emails)

        # Update the record using a queryset with the filter condition
        frenchise_employee_register_model.objects.filter(id=empIds).update(email=emails, employee_id=employeeuiid)

        # employee_user = getEmployee.user.username
        # email = getEmployee.email
        # e_fm = Employee_application_form(request.POST, instance=getEmployee)
        # if e_fm.is_valid():
        #     e_fm.save()

        # else:
        getEmployee = frenchise_employee_register_model.objects.get(id=empid)
        e_fm = Employee_application_form(instance=getEmployee)

        return render(request,'frenchise/edit_employee_dashboard.html', {'employeData':getEmployee})



    loginUser = request.user.username
    # getEmployee = frenchise_employee_register_model.objects.filter(id=empid)
    getEmployee = frenchise_employee_register_model.objects.get(id=empid)
    employee_user = getEmployee.user.username
    email = getEmployee.email


    if loginUser == employee_user:
        
        return render(request, 'frenchise/edit_employee_dashboard.html',{'employeData':getEmployee})
    


#Admin Franchise Dashboard

def frenchise_dashboard_admin_view(request):
    return render(request, 'frenchise/frenchise_dashboard_admin.html')

def frenchise_employee_admin_view(request):
    return render(request, 'frenchise/frenchise_employee_admin.html')

@login_required
def appllyloan(request):
    if request.method == 'POST':
        users = request.user
        name = request.POST.get('name')
        emails = request.POST.get('email')
        amount = request.POST.get('amount')
        type = request.POST.get('type')
        number = request.POST.get('number')
        pan = request.POST.get('pan')
        print([name,emails,amount,type,number])
        createloan = Loan.objects.create(user=users,clientName=name,type=type,PAN=pan,number=number,amount=amount,email=emails)
        
        return render(request,'frenchise/apply_loan.html')

    return render(request,'frenchise/apply_loan.html')

#Employee overview 
def employee_overview_view(request):
    return render(request, 'frenchise/employee_overview.html')




# def frenchise_chart_view(request):
#     if request.method == 'POST':
#         print("date from to")

#     total = {
#         'toatal':"455",
#         'success':"105"
#     }
#     chart = {
#         'loan':'255',
#         'insurance':'200',
#         'demat':'204',
#         'mutualFund':'255',
#     }