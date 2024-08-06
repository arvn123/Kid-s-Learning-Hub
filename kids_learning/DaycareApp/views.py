from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import datetime

from django.views.decorators.cache import cache_control

from AdminApp.models import tbl_category, tbl_subcategory, tbl_daycare
from DaycareApp.models import tbl_progress
from GuestApp.models import tbl_parent
from ParentApp.models import tbl_application
import smtplib
from email.message import EmailMessage


# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        return render(request, "Daycare/index.html")
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def applicationrequest(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        apprequests=tbl_application.objects.filter(application_status="requested",daycare_id__login_id=request.session['loginid'])
        return render(request, "Daycare/applicationrequest.html",{'apprequests':apprequests})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def applicationdetails(request,id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        details=tbl_application.objects.select_related('parent_id','daycare_id').get(application_id=id)
        return render(request, "Daycare/applicationdetails.html",{'details':details})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def confirmrequest(request,id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        aob=tbl_application.objects.get(application_id=id)
        aob.application_status="confirmed"
        aob.save()
        cid = request.POST.get('cid')
        # return HttpResponse(cid)
        msg = EmailMessage()
        obj = tbl_daycare.objects.get(daycare_id=aob.daycare_id_id)
        data = 'Your Admission is Approved '+obj.branch_name
        msg.set_content(data)
        msg['Subject'] = "Confirmation From daycare"
        msg['from'] = 'aravindhari2003@gmail.com'

        obj1 = tbl_parent.objects.get(parentid=aob.parent_id_id)

        msg['To'] = obj1.email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('aravindhari2003@gmail.com', 'ybjk uude gkdu sygm')
            smtp.send_message(msg)

        return HttpResponse("<script>alert('Successfully send Mail');window.location='/DaycareApp/applicationrequest';</script>")
    #return redirect('/DaycareApp/applicationrequest')

    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def rejectrequest(request,id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        aob = tbl_application.objects.get(application_id=id)
        aob.application_status = "Rejected"
        aob.save()
        return HttpResponse("<script>alert('Successfully Rejected..');window.location='/DaycareApp/applicationrequest';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def applicationconfirmed(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        appconfirmed=tbl_application.objects.filter(application_status="paid",daycare_id__login_id=request.session['loginid'])
        return render(request, "Daycare/applicationconfirmed.html",{'appconfirmed':appconfirmed})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def appconfirmdetails(request,id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        details=tbl_application.objects.select_related('parent_id','daycare_id').get(application_id=id)
        return render(request, "Daycare/appconfirmdetails.html",{'details':details})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def progress(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == "POST":
            pob=tbl_progress()
            pob.subcategoryid=tbl_subcategory.objects.get(subcategoryid=request.POST.get('subcategory'))
            pob.daycareid=tbl_daycare.objects.get(login_id__LoginId=request.session['loginid'])
            pob.applicationid=tbl_application.objects.get(application_id=request.POST.get('application'))
            pob.description=request.POST.get('description')
            pob.grade=request.POST.get('grade')
            if tbl_progress.objects.filter(applicationid=request.POST.get('application'),pro_date=datetime.now().date(),subcategoryid=request.POST.get('subcategory')).exists():
                return HttpResponse("<script>alert('Already Exists...');window.location='/DaycareApp/progress'</script>")
            else:
                pob.save()
                return HttpResponse("<script>alert('Successfully Added..');window.location='/DaycareApp/progress';</script>")
        details=tbl_category.objects.all()
        kids=tbl_application.objects.filter(application_status='paid' , daycare_id__login_id__LoginId=request.session['loginid'])
        #return HttpResponse(request.session['loginid'])
        progress=tbl_progress.objects.filter(daycareid_id__login_id_id=request.session['loginid'],applicationid__application_status="paid")
        return render(request, "Daycare/progress.html",{'details':details,'kids':kids,'progress':progress})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deleteprogress(request,id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        obj=tbl_progress.objects.get(progressid=id)
        obj.delete()
        return HttpResponse("<script>alert('Successfully Deleted..');window.location='/DaycareApp/progress';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillsubcategory(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        id = int(request.POST.get("did"))
        subcategory = tbl_subcategory.objects.filter(categoryid=id).values()
        return JsonResponse(list(subcategory), safe=False)
    else:
        return HttpResponse(
            "<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")

def logout(request):
    if "loginid" in request.session:
        request.session.clear()  # This will delete all session variables
        return HttpResponse("<script>alert('successfully logout');window.location='/';</script>");

