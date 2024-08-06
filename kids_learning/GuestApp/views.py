import random
import smtplib
import string
from email.message import EmailMessage

from django.http import HttpResponse
from django.shortcuts import render, redirect

from AdminApp.models import tbl_district, tbl_location
from GuestApp.models import login, tbl_parent


# Create your views here.
def index(request):
    return render(request, "Guest/index.html")


def loginnew(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        passw = request.POST.get('pass')
        if login.objects.filter(username=uname, password=passw).exists():
            lob = login.objects.get(username=uname, password=passw)
            #return HttpResponse(lob.username)
            request.session['username'] = lob.username
            request.session['loginid'] = lob.LoginId
            if lob.role == "Admin":
                return redirect('/AdminApp/adminhome')
            elif lob.role == "parent":
                return redirect('/ParentApp/parenthome')
            elif lob.role == "Daycare":
                return redirect('/DaycareApp/daycarehome')
            else:
                return render(request, 'Guest/index.html', {'error': 'Incorrect Username or Password'})
        else:
            return render(request, 'Guest/login.html', {'error': 'Incorrect Username or Password'})
    else:
        return render(request, 'Guest/login.html')

def parent(request):
    if request.method == 'POST':
        cob = login()
        cob.username = request.POST.get('username')
        cob.password = request.POST.get('password')
        cob.role = 'parent'
        cob.save()
        lob = tbl_parent()
        lob.parentname = request.POST.get('name')
        lob.email = request.POST.get('email')
        lob.phno = request.POST.get('phno')
        lob.address = request.POST.get('address')
        lob.locationid = tbl_location.objects.get(locationid=request.POST.get("location"))
        lob.loginid = cob
        lob.save()
        return HttpResponse("<script>alert('Successfully added..');window.location='/parent';</script>")
    district = tbl_district.objects.all()
    return render(request, 'Guest/parentreg.html', {'district': district})

def forgotpassword(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        if login.objects.filter(username=uname).exists():
            lg=login.objects.get(username=uname)
            lid=lg.LoginId
            cust=tbl_parent.objects.get(loginid=lid)
            email=cust.email
            parentname=cust.parentname
            characters = string.ascii_letters + string.digits
            random_number = ''.join(random.choice(characters) for _ in range(8))
            #return HttpResponse(email)
            lg.password=random_number
            lg.save()
            msg=EmailMessage()
            msg.set_content(f'Hi {parentname},Your new password to login in is {random_number}')
            msg['Subject']="Forgot Password ?"
            msg['from']='aravindhari2003@gmail.com'
            msg['To']={email}
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                smtp.login('aravindhari2003@gmail.com','ybjk uude gkdu sygm')
                smtp.send_message(msg)
            return HttpResponse("<script>alert('Login with new password in youremail');window.location='/login';</script>")
        return HttpResponse("<script>alert('No datafound');window.location='/forgotpassword';</script>")
    return render(request,"Guest/forgotpassword.html")
