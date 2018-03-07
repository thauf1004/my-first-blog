from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^menu/$', views.menu_list, name='menu_list'),
    url(r'^system/menu/$', views.menu_list, name='menu_list'),
]