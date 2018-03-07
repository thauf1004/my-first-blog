from django.shortcuts import render , get_object_or_404 , redirect
from system.models import Menu

def menu_list(request):
# Create your views here.
    menus = Menu.objects.all()
    print(menus)
    return render ( request , 'system/menu_list.html' , {'menus': menus} )
