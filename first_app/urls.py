from django.urls import path
from first_app import views

urlpatterns = [
    path("sample/", views.sample, name="sample"),
    path('add/<int:a>/<int:b>', views.addition, name='addition'),
    path('sub/', views.subtraction, name='subtraction'),
    path('mul/', views.mul, name='mul'),
    path('mulres', views.mulres, name='mulres'),
    path('employees/', views.employees, name='employees'),
    path('addemp',views.addemp,name='addemp'),
    path('newemp',views.newemp,name='newemp')
    
]