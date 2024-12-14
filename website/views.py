from django.shortcuts import render
from adminpanel.models import website_header

def index(request):
    # header_info = website_header.objects.all()
    header_info = website_header.objects.filter(is_active = True).order_by('-id')[:4]
    context = {
        'header_info':header_info
    }
    return render(request,'website/index.html',context)


