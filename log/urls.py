from django.urls import path

from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('loginhome/',views.loginhome, name='loginhome'),
    path('logout/',views.logout, name='logout'),
    path('adminlog/',views.adminlogin, name='adminlogin'),
    path('adminhome/',views.adminhome, name='adminhome'),
    path('adminedit/<int:id>/',views.adminedit, name='adminedit'),
    path('adduser/',views.adduser, name='adduser'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('adminlogout/',views.adminlogout, name='adminlogout')
    
]