from django.urls import path
from adminpanel import views

urlpatterns = [
 path('registration',views.reg,name='registration'),
 path('login_user',views.login_user,name='login_user'),
 path('logout_user',views.logout_user,name='logout_user'),
 path('dashboard',views.dashboard,name='dashboard'),
 path('create/header_info',views.create_header,name='create_header_info'),
 path('show/header',views.show_header,name='show_header'),
 path('header_active/<int:id>',views.header_active,name='header_active'),
 path('header_dactive/<int:id>',views.header_dactive,name='header_dactive'),
]
