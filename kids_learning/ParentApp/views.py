from django.db.models import Max
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_control

from AdminApp.models import tbl_district, tbl_location, tbl_daycare
from DaycareApp.models import tbl_progress, tbl_payment
from GuestApp.models import tbl_parent, login
from ParentApp.models import tbl_application


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def parenthome(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        return render(request, "Parent/index.html")
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admission(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        district=tbl_district.objects.all()
        return render(request, "Parent/admission.html",{'district':district})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def filllocation(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        id = int(request.POST.get("did"))
        location = tbl_location.objects.filter(districtid=id).values()
        return JsonResponse(list(location), safe=False)
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def filldaycare(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        id = int(request.POST.get("did"))
        daycare = tbl_daycare.objects.filter(location_id=id).values()
        return JsonResponse(list(daycare), safe=False)
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admissiondetails(request,id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        max_value = tbl_application.objects.filter(daycare_id=tbl_daycare.objects.get(daycare_id=id)).aggregate(max_value=Max('application_no'))['max_value']
        return render(request, "Parent/application.html", {'daycareid': id,'max_value':max_value})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def application(request,id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        aob=tbl_application()
        aob.child_name=request.POST.get("child_name")
        aob.child_age = request.POST.get("child_age")
        aob.child_gender = request.POST.get("child_gender")
        aob.child_image=request.FILES['image']
        aob.child_healthdetails = request.POST.get("child_healthdetails")
        aob.application_status = "requested"
        applicationcount=tbl_application.objects.filter(daycare_id=tbl_daycare.objects.get(daycare_id=id)).count()
        if applicationcount == 0:
            aob.application_no = 1
        else:
            max_value = tbl_application.objects.filter(daycare_id=tbl_daycare.objects.get(daycare_id=id)).aggregate(max_value=Max('application_no'))['max_value']
            aob.application_no = max_value+1
        aob.parent_id=tbl_parent.objects.get(loginid_id=int(request.session['loginid']))
        aob.daycare_id = tbl_daycare.objects.get(daycare_id=id)
        aob.save()
        return HttpResponse("<script>alert('Successfully Requested..');window.location='/ParentApp/admission';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def confirmdetails(request, details=None):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        details = tbl_application.objects.filter(application_status="confirmed",parent_id__loginid__LoginId=request.session['loginid'])
        return render(request, "Parent/confirmdetails.html", {'details':details})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewmore(request,id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        details = tbl_application.objects.get(application_id=id)
        return render(request, "Parent/viewmore.html", {'details':details})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def payment(request,id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method=="POST":
            pob=tbl_payment()
            pob.daycare_id=request.POST.get('daycareid')
            pob.application_id=id
            pob.status="paid"
            pob.save()
            aob = tbl_application.objects.get(application_id=id)
            aob.application_status="paid"
            aob.save()

            return HttpResponse("<script>alert('Successfully Paid..');window.location='/ParentApp/confirmdetails';</script>")
        aob=tbl_application.objects.get(application_id=id)
        dob=tbl_daycare.objects.get(daycare_id=aob.daycare_id.daycare_id)
        return render(request, "Parent/payment.html",{'dob':dob,'aob':aob})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def progresskids(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        applications=tbl_application.objects.filter(application_status='paid',parent_id__loginid__LoginId=request.session['loginid'])
        return render(request, "Parent/progresskids.html", {'applications': applications})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def progressdetails(request,id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        progress=tbl_progress.objects.filter(applicationid_id=id)
        return render(request, "Parent/progressdetails.html", {'progress': progress})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



def logout(request):
    if "loginid" in request.session:
        request.session.clear()  # This will delete all session variables
        return HttpResponse("<script>alert('successfully logout');window.location='/';</script>");


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def parentprofile(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        #login = Tbl_login.objects.filter(loginid=id)
        parent = tbl_parent.objects.get(loginid_id=request.session['loginid'])
        return render(request, "Parent/parentprofile.html", {'parent':parent})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editprofile(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == 'POST':

            parent=tbl_parent.objects.get(loginid_id=request.session['loginid'])
            #return HttpResponse(request.session['loginid'])
            parent.parentname = request.POST.get('parentname')
            parent.email = request.POST.get('email')
            parent.phno = request.POST.get('phno')
            parent.address = request.POST.get('Address')
            # parent.district = tbl_district.objects.get(districtid=request.POST.get('district'))
            # parent.location=tbl_location.objects.get(locationid=request.POST.get('location'))
            parent.save()
            return HttpResponse("<script>alert('Successfully updated...');window.location='../parentprofile'</script>")

        parent=tbl_parent.objects.get(loginid_id=request.session['loginid'])
        # district=tbl_district.objects.all()
        # location= tbl_location.objects.all()
        return render(request, 'parent/editprofile.html',{ 'parent':parent})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def filllocation(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        id = int(request.POST.get("did"))
        location = tbl_location.objects.filter(districtid=id).values()
        return JsonResponse(list(location), safe=False)
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def changepassword(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method=='POST':
            uname=request.POST.get("username")
            password=request.POST.get("password")
            newpwd=request.POST.get("newpwd")
            connewpwd=request.POST.get("connewpwd")
            if login.objects.filter(username=uname,password=password).exists():
                lo=login.objects.get(username=uname,password=password)
                if newpwd == connewpwd:
                    lo.password=newpwd
                    lo.save()
                    return HttpResponse("<script>alert('Successfully updated!!');window.location='/ParentApp/parenthome/'</script>")
                return HttpResponse("<script>alert('Password Mismatch !!');window.location='/ParentApp/changepassword'</script>")
            return HttpResponse("<script>alert('Invalid Username or  Password!!');window.location='/ParentApp/changepassword'</script>")
        return render(request,"Parent/changepassword.html")
    else:
         return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")
