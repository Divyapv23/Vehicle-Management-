from django.shortcuts import render,redirect
from Vehicleapp.models import Vehicle,adminlogin


# Create your views here.

def vehiclepage(request):
    data = Vehicle.objects.all()
    return render(request, "vehicledis.html", {'data': data})

def vehdisedit(request):
    data=Vehicle.objects.all()
    return render(request,"vehicle.html",{'data':data})

def vehicleedit(request,dataid):
    data=Vehicle.objects.get(id=dataid)
    return render(request,"updatelist.html",{'data':data})

def vehicleupdate(request,dataid):
    if request.method=="POST":
        nu=request.POST.get('vname')
        ty=request.POST.get('vtype')
        md=request.POST.get('vmodel')
        ds=request.POST.get('vdescription')
        Vehicle.objects.filter(id=dataid).update(number=nu,v_type=ty,model=md,description=ds)
        return redirect(vehdisedit)

def loginpage(request):
    return render(request,"login.html")

def logindetails(request):
    if request.method=="POST":
        em=request.POST.get('email')
        ps=request.POST.get('pass')
        if adminlogin.objects.filter(Mail=em,Password=ps).exists():
            request.session['email']=em
            request.session['pass']=ps
            return redirect(vehdisedit)
        else:
            return redirect(loginpage)
    return redirect(loginpage)
