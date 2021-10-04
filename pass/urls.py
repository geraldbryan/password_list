from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.passform, name = 'password-form'),
    path('register/', views.register, name = "register-user"),
    path('login/',auth_views.LoginView.as_view(template_name='pass/login.html'), name="login-user"),
    path('logout/',auth_views.LogoutView.as_view(template_name='pass/logout.html'), name="logout-user"),
    
    path('socialmedia/',views.socmed, name="socmed-user"),
    path('socialmedia_detail/<str:pk_passlist>/', views.socmed_detail, name= 'socmed-detail'),
    path('socialmedia_update/<str:pk_passlist>/', views.socmed_edit, name= 'socmed-edit'),
    path('socialmedia_delete/<str:pk_passlist>/', views.socmed_delete, name= 'socmed-delete'),

    path('email/',views.email, name="email-user"),
    path('email_detail/<str:pk_passlist>/', views.email_detail, name= 'email-detail'),
    path('email_update/<str:pk_passlist>/', views.email_edit, name= 'email-edit'),
    path('email_delete/<str:pk_passlist>/', views.email_delete, name= 'email-delete'),

    path('bank/',views.bank, name="bank-user"),
    path('bank_detail/<str:pk_passlist>/', views.bank_detail, name= 'bank-detail'),
    path('bank_update/<str:pk_passlist>/', views.bank_edit, name= 'bank-edit'),
    path('bank_delete/<str:pk_passlist>/', views.bank_delete, name= 'bank-delete'),

    path('creditcard/',views.credcard, name="credcard-user"),
    path('creditcard_detail/<str:pk_passlist>/', views.credcard_detail, name= 'creditcard-detail'),
    path('creditcard_update/<str:pk_passlist>/', views.credcard_edit, name= 'creditcard-edit'),
    path('creditcard_delete/<str:pk_passlist>/', views.credcard_delete, name= 'creditcard-delete'),

    path('health/',views.health, name="health-user"),
    path('health_detail/<str:pk_passlist>/', views.health_detail, name= 'health-detail'),
    path('health_update/<str:pk_passlist>/', views.health_edit, name= 'health-edit'),
    path('health_delete/<str:pk_passlist>/', views.health_delete, name= 'health-delete'),

    path('trading/',views.trading, name="trading-user"),
    path('trading_detail/<str:pk_passlist>/', views.trading_detail, name= 'trading-detail'),
    path('trading_update/<str:pk_passlist>/', views.trading_edit, name= 'trading-edit'),
    path('trading_delete/<str:pk_passlist>/', views.trading_delete, name= 'trading-delete'),

    path('ecommerce/',views.ecom, name="bank-user"),
    path('ecommerce_detail/<str:pk_passlist>/', views.ecom_detail, name= 'ecom-detail'),
    path('ecommerce_update/<str:pk_passlist>/', views.ecom_edit, name= 'ecom-edit'),
    path('ecommerce_delete/<str:pk_passlist>/', views.ecom_delete, name= 'ecom-delete'),

    path('other/',views.bank, name="bank-user"),
    path('other_detail/<str:pk_passlist>/', views.other_detail, name= 'other-detail'),
    path('other_update/<str:pk_passlist>/', views.other_edit, name= 'other-edit'),
    path('other_delete/<str:pk_passlist>/', views.other_delete, name= 'other-delete'),
]