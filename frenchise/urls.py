from django.contrib import admin
from django.urls import path, include
from frenchise import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm,  MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm




urlpatterns = [
    
    path('', views.index, name='home'),
    path('about/', views.about_view, name= 'about'),
    path('services/', views.Services_view, name= 'services'),
    path('blog/', views.blog_view, name= 'blog'),
    path('blog-details/', views.blog_details_view, name= 'blog_details'),
    path('contact/', views.contact_view, name= 'contact'),


    path('emp-details/<int:empid>/', views.edit_employee_dashboard_view, name= 'emp_details'),
    path('register/', views.frenchise_registration_view, name= 'register'),
    path('profile/', views.profile, name= 'profile'),

    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('apply-loan/', views.apply_loan_view, name= 'apply_loan'),

    path('Employee-registration/', views.employee_view, name= 'emp_registration'),
    
    path('employee/', views.employee_view, name= 'employee'),
    path('confirmation/', views.frenchise_confirmation, name= 'confirmation'),

    path('frenchise-application/', views.frenchise_application_view, name= 'applyfrenchise'),
    # path('frenchise-application/', views.frenchise_apply_view, name= 'a_frenchise'),


    #Employee URLS
    path('emp-dashboard/', views.employee_dashboard_view, name= 'e_dashboard'),
    path('edit-emp-dashboard/', views.employee_dashboard_view, name= 'edit_e_dashboard'),






    #Authentication URLS
    path('accounts/login/',auth_views.LoginView.as_view(template_name='frenchise/login.html',authentication_form=LoginForm),name='login'),
    #  3-Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    #Password change
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='frenchise/passwordchange.html',
        form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='frenchise/passwordchangedone.html'),name='passwordchangedone'),
    # 5-password reset
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='frenchise/password_reset.html',
        form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='frenchise/password_reset_done.html')
        ,name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='adminss/password_reset_confirm.html'
        ,form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='frenchise/password_reset_complete.html')
        ,name='password_reset_complete'),
]
