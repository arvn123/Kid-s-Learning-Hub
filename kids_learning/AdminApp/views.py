import xlwt
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.views import View

from AdminApp.models import tbl_district, tbl_category, tbl_location, tbl_subcategory, tbl_daycare
from DaycareApp.models import tbl_payment
from GuestApp.models import login, tbl_parent
from django.views.decorators.cache import cache_control

from ParentApp.models import tbl_application


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Adminhome(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        return render(request, "Admin/index.html", {'Loginid': logid, 'Logname': logname})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def district(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == "POST":
            cob = tbl_district()
            cob.districtname = request.POST.get('districtname')
            if tbl_district.objects.filter(districtname=request.POST.get('districtname')).exists():
                return HttpResponse("<script>alert('Already Exists...');window.location='../district';</script>")
            else:
                cob.save()
                return HttpResponse("<script>alert('Successfully Added...');window.location='../district';</script>")

        else:
            # return HttpResponse("haii")
            district = tbl_district.objects.all()
            return render(request, 'Admin/district.html', {'district': district})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editdistrict(request, id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == 'POST':
            districtname = request.POST.get('districtname')
            district = tbl_district.objects.get(districtid=id)
            district.districtname = districtname
            district.save()
            return HttpResponse("<script>alert('Successfully updated...');window.location='../district'</script>")
        district = tbl_district.objects.get(districtid=id)
        return render(request, 'admin/editdistrict.html', {'district': district})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletedistrict(request, id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        district = tbl_district.objects.get(districtid=id)
        district.delete()
        return HttpResponse("<script>alert('Successfully deleted...');window.location='../district'</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def category(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == "POST":
            cob = tbl_category()
            cob.categoryname = request.POST.get('categoryname')
            cob.categoryimage = request.FILES['image']
            if tbl_category.objects.filter(categoryname=request.POST.get('categoryname')).exists():
                return HttpResponse("<script>alert('Already Exists...');window.location='../category';</script>")
            else:
                cob.save()
                return HttpResponse("<script>alert('Successfully Added...');window.location='../category';</script>")

        else:
            category = tbl_category.objects.all()
            return render(request, 'Admin/category.html', {'category': category})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editcategory(request, id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == 'POST':
            categoryname = request.POST.get('categoryname')
            category = tbl_category.objects.get(categoryid=id)
            category.categoryname = categoryname
            if len(request.FILES) == 0:
                category.categoryimage = request.POST.get('pimage')
            else:
                category.categoryimage = request.FILES['pimagenew']
            category.save()
            return HttpResponse("<script>alert('Successfully updated...');window.location='../category'</script>")
        category = tbl_category.objects.get(categoryid=id)
        return render(request, 'admin/editcategory.html', {'category': category})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletecategory(request, id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        category = tbl_category.objects.get(categoryid=id)
        category.delete()
        return HttpResponse("<script>alert('Successfully deleted...');window.location='../category'</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def location(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == "POST":
            cob = tbl_location()
            cob.locationname = request.POST.get('locationname')
            if tbl_location.objects.filter(locationname=request.POST.get('locationname')).exists():
                return HttpResponse("<script>alert('Already Exists...');window.location='../location'</script>")
            else:
                cob.districtid = tbl_district.objects.get(districtid=request.POST.get('districtid'))
                cob.save()  # insert query
                return HttpResponse("<script>alert('Successfully Added...');window.location='../location'</script>")

        else:
            district = tbl_district.objects.all()
            row = tbl_district.objects.first()
            location = tbl_location.objects.filter(districtid=row.districtid)
            return render(request, 'admin/location.html', {'location': location, 'district': district, 'row': row})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editlocation(request, id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == 'POST':
            locationname = request.POST.get('locationname')
            dist = request.POST.get('districtid')
            location = tbl_location.objects.get(locationid=id)
            location.locationname = locationname
            location.districtid = tbl_district.objects.get(districtid=dist)

            location.save()
            return HttpResponse("<script>alert('Successfully updated...');window.location='../location'</script>")
        location = tbl_location.objects.get(locationid=id)
        district = tbl_district.objects.all()
        return render(request, 'admin/editlocation.html', {'location': location, 'district': district})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletelocation(request, id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        location = tbl_location.objects.get(locationid=id)
        location.delete()
        return HttpResponse("<script>alert('Successfully deleted...');window.location='../location'</script>")
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
def subcategory(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == "POST":
            cob = tbl_subcategory()
            cob.subcategoryname = request.POST.get('subcategoryname')
            cob.subcategoryimage = request.FILES['subimage']
            if tbl_subcategory.objects.filter(subcategoryname=request.POST.get('subcategoryname')).exists():
                return HttpResponse("<script>alert('Already Exists...');window.location='../subcategory'</script>")
            else:
                cob.categoryid = tbl_category.objects.get(categoryid=request.POST.get('categoryid'))
                cob.save()  # insert query
                return HttpResponse("<script>alert('Successfully Added...');window.location='../subcategory'</script>")

        else:
            category = tbl_category.objects.all()
            row = tbl_category.objects.first()
            subcategory = tbl_subcategory.objects.filter(categoryid=row.categoryid)
            return render(request, 'admin/subcategory.html', {'category': category, 'subcategory': subcategory, 'row': row})
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
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editsubcategory(request, id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == 'POST':
            subcategoryname = request.POST.get('subcategoryname')
            category = request.POST.get('categoryid')
            subcategory = tbl_subcategory.objects.get(subcategoryid=id)
            subcategory.subcategoryname =subcategoryname
            subcategory.categoryid = tbl_category.objects.get(categoryid=category)
            if len(request.FILES) == 0:
                subcategory.subcategoryimage = request.POST.get('pimage')
            else:
                subcategory.subcategoryimage = request.FILES['pimagenew']
            subcategory.save()
            return HttpResponse("<script>alert('Successfully updated...');window.location='../subcategory'</script>")
        subcategory = tbl_subcategory.objects.get(subcategoryid=id)
        category= tbl_category.objects.all()
        return render(request, 'admin/editsubcategory.html', {'category': category, 'subcategory': subcategory})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletesubcategory(request, id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        subcategory = tbl_subcategory.objects.get(subcategoryid=id)
        subcategory.delete()
        return HttpResponse("<script>alert('Successfully deleted...');window.location='../subcategory'</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def daycare(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == 'POST':
            cob = login()
            cob.username = request.POST.get('username')
            cob.password = request.POST.get('password')
            cob.role = 'Daycare'

            lob = tbl_daycare()
            lob.daycare_name = request.POST.get('daycarename')
            lob.branch_name = request.POST.get('branch_name')
            lob.daycare_image = request.FILES['image']
            lob.daycare_contact = request.POST.get('daycare_contact')
            lob.description = request.POST.get('description')
            lob.daycare_email = request.POST.get('email')
            lob.daycare_landmark = request.POST.get('landmark')
            lob.daycare_pincode = request.POST.get('pincode')
            lob.daycare_map = request.POST.get('map')
            lob.application_fee = request.POST.get('applicationfees')
            lob.monthly_fee = request.POST.get('monthlyfees')
            lob.location_id = tbl_location.objects.get(locationid=request.POST.get("location"))

            if tbl_daycare.objects.filter(location_id=tbl_location.objects.get(locationid=request.POST.get("location"))).exists():
                return HttpResponse("<script>alert('Already Exists...');window.location='/AdminApp/daycare'</script>")
            else:
                cob.save()
                lob.login_id = cob
                lob.save()
            return HttpResponse("<script>alert('Successfully added..');window.location='/AdminApp/daycare';</script>")
        district = tbl_district.objects.all()
        return render(request, 'Admin/daycare.html', {'district': district})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editdaycare(request, id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        if request.method == 'POST':
            lob = tbl_daycare.objects.get(daycare_id=id)
            lob.daycare_name = request.POST.get('daycarename')
            lob.branch_name = request.POST.get('branch_name')
            lob.daycare_contact = request.POST.get('daycare_contact')
            lob.description = request.POST.get('description')
            lob.daycare_email = request.POST.get('email')
            lob.daycare_landmark = request.POST.get('landmark')
            lob.daycare_pincode = request.POST.get('pincode')
            lob.daycare_map = request.POST.get('map')
            lob.application_fee = request.POST.get('applicationfees')
            lob.monthly_fee = request.POST.get('monthlyfees')
            cob=login.objects.get(LoginId=lob.login_id_id)
            cob.username=request.POST.get('username')
            cob.password = request.POST.get('password')
            if len(request.FILES) == 0:
                lob.daycare_image = request.POST.get('pimage')
            else:
                lob.daycare_image = request.FILES['pimagenew']
            cob.save()
            lob.save()
            return HttpResponse("<script>alert('Successfully updated...');window.location='../daycare'</script>")
        daycare = tbl_daycare.objects.get(daycare_id=id)
        return render(request, 'admin/editdaycare.html', {'daycare': daycare})
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletedaycare(request, id):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        daycare = tbl_daycare.objects.get(daycare_id=id)
        log = login.objects.get(LoginId=daycare.login_id_id)
        log.delete()
        daycare.delete()
        return HttpResponse("<script>alert('Successfully deleted...');window.location='../daycare'</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def filldaycare(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        id = int(request.POST.get("did"))
        daycare = tbl_daycare.objects.select_related('login_id').filter(location_id=id).values('branch_name','daycare_email','daycare_contact','description','login_id__username','login_id__password','daycare_image','application_fee','monthly_fee','daycare_landmark','daycare_pincode','daycare_id','daycare_map')
        return JsonResponse(list(daycare), safe=False)
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pie_chart(request):
    logid = request.session.get('loginid')
    logname = request.session.get('username')
    if logid:
        labels = []
        data = []
        queryset = tbl_subcategory.objects.values('categoryid__categoryname').annotate(total_category=Count('categoryid'))
        for s in queryset:
            labels.append(s['categoryid__categoryname'])
            data.append(s['total_category'])

        return render(request, 'Admin/categorypiechart.html', {
            'labels': labels,
            'data': data,
        })
    else:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pie_chart1(request):
        logid = request.session.get('loginid')
        logname = request.session.get('username')
        if logid:
            labels = []
            data = []
            queryset = tbl_application.objects.values('child_name').annotate(total_child=Count('application_id'))
            for s in queryset:
                labels.append(s['child_name'])
                data.append(s['total_child'])

            return render(request, 'Admin/daycarepiechart.html', {
                'labels': labels,
                'data': data,
            })
        else:
            return HttpResponse(
                "<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")


#location based application count
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def location_application(request):
        logid = request.session.get('loginid')
        logname = request.session.get('username')
        if logid:
            labels = []
            data = []
            queryset = tbl_application.objects.values('parent_id__locationid__locationname').annotate(total_child=Count('application_id')).order_by('-total_child')[:5]
            for s in queryset:
                labels.append(s['parent_id__locationid__locationname'])
                data.append(s['total_child'])

            return render(request, 'Admin/location_application.html', {
                'labels': labels,
                'data': data,
            })
        else:
            return HttpResponse(
                "<script>alert('Authentication Required Please loginfirst');window.location='/login';</script>")

def datewise_application(request):
    return render(request, 'Admin/datewiseexcel.html')

class ExportExceldatewise(View):
    def post(self, request):
        fdate = request.POST.get('fdate')
        tdate = request.POST.get('tdate')
        #return HttpResponse(fdate)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="applicationdetails.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['Admission No', 'Kid Name', 'Age','Gender','Health Details']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        details = tbl_payment.objects.select_related('application').filter(pdate__range=(fdate, tdate),status="paid").values_list('application__application_no','application__child_name', 'application__child_age', 'application__child_gender', 'application__child_healthdetails')
        # return HttpResponse(list(details))

        for row in details:
            row_num += 1
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)


        wb.save(response)
        return response


#Excel Export Code

class ExportExcelparent(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="parentlist.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['Name', 'Email', 'Contact No.', 'address']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        queryset = tbl_parent.objects.all().values_list('parentname', 'email', 'phno', 'address')
        for row in queryset:
            row_num += 1
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response

class ExportExcelchild(View):
        def get(self, request):
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="studentlist.xls"'

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Sheet1')

            # Define the column headings
            row_num = 0
            columns = ['Name', 'Age', 'Gender', 'ApplicationNo.']
            for col_num, column_title in enumerate(columns):
                ws.write(row_num, col_num, column_title)

            # Query the data from your model, and write it to the worksheet
            queryset = tbl_application.objects.all().values_list('child_name', 'child_age', 'child_gender', 'application_no')
            for row in queryset:
                row_num += 1
                for col_num, cell_value in enumerate(row):
                    ws.write(row_num, col_num, cell_value)

            wb.save(response)
            return response


def logout(request):
    if "LoginId" in request.session:
        del request.session["LoginId"]
        del request.session['username']
        return redirect('/')
