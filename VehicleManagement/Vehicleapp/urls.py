from django.urls import path
from Vehicleapp import views

urlpatterns = [
    path('vehiclepage/', views.vehiclepage, name="vehiclepage"),
    path('vehdisedit/',views.vehdisedit,name="vehdisedit"),
    path('vehicleedit/<int:dataid>',views.vehicleedit,name="vehicleedit"),
    path('vehicleupdate/<int:dataid>',views.vehicleupdate,name="vehicleupdate"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('logindetails/',views.logindetails,name="logindetails")



]
