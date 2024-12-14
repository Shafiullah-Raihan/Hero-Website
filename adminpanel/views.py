from django.shortcuts import render,redirect,HttpResponse
from adminpanel.models import User, website_header
from django.contrib.auth import login,logout,authenticate


def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'admin/index.html')
    else:
        return redirect('login_user')
    

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if password_1 != password_2:
            return redirect('registration')
        else:
            user_reg = User.objects.create_user(username,email,password_1)
            user_reg.first_name = password_2
            user_reg.save()
            return redirect('login_user')
    return render(request,'admin/user_panel/reg.html')

def login_user(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('psw')
        user_check = authenticate(username = a, password = b)

        if user_check != None:
            login(request,user_check)
            return redirect('dashboard')
        else:
            return redirect('login_user')
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request,'admin/user_panel/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login_user')
    
def create_header(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.FILES['image']

            create_header = website_header(
                title = title,
                description = description,
                images = image
            )
            create_header.save()

        return render(request,'admin/header_info/add_header.html')
    else:
        return redirect('login_user')

def show_header(request):
    if request.user.is_authenticated:
        header_show = website_header.objects.all()
        context = {
            'header_show':header_show,
        }
        return render(request,'admin/header_info/show_header.html',context)
    else:
        return redirect('login_user')
    
def header_active(request,id):
    if request.user.is_authenticated:
        header_activate = website_header.objects.get(id=id)
        header_activate.is_active = True
        header_activate.save()
        return redirect('show_header')
    else:
        return redirect('login_user')

def header_dactive(request,id):
    if request.user.is_authenticated:
        header_dactivate = website_header.objects.get(id=id)
        header_dactivate.is_active = False
        header_dactivate.save()
        return redirect('show_header')
    else:
        return redirect('login_user')
    

