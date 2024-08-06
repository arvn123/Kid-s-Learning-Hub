from django.urls import path
from AdminApp import views
from AdminApp.views import ExportExcelparent, ExportExcelchild,ExportExceldatewise


urlpatterns = [
    path('adminhome/', views.Adminhome, name="adminhome"),
    path('district/', views.district, name='district'),
    path('editdistrict/<id>', views.editdistrict, name='editdistrict'),
    path('deletedistrict/<id>', views.deletedistrict, name='deletedistrict'),
    path('category/', views.category, name='category'),
    path('editcategory/<id>', views.editcategory, name='editcategory'),
    path('deletecategory/<id>', views.deletecategory, name='deletecategory'),
    path('location/', views.location, name='location'),
    path('editlocation/<id>', views.editlocation, name='editlocation'),
    path('deletelocation/<id>', views.deletelocation, name='deletelocation'),
    path('filllocation/', views.filllocation, name='filllocation'),
    path('fillsubcategory/', views.fillsubcategory, name='fillsubcategory'),
    path('subcategory/', views.subcategory, name='subcategory'),
    path('editsubcategory/<id>', views.editsubcategory, name='editsubcategory'),
    path('deletesubcategory/<id>', views.deletesubcategory, name='deletesubcategory'),
    path('daycare/', views.daycare, name='daycare'),
    path('editdaycare/<id>', views.editdaycare, name='editdaycare'),
    path('deletedaycare/<id>', views.deletedaycare, name='deletedaycare'),
    path('filldaycare/', views.filldaycare, name='filldaycare'),
    path('pie_chart/', views.pie_chart, name='pie_chart'),
    path('pie_chart1/', views.pie_chart1, name='pie_chart1'),
    path('export_excel/', ExportExcelparent.as_view(), name='export_excel'),
    path('export_excel1/', ExportExcelchild.as_view(), name='export_excel1'),
    path('logout/', views.logout, name='logout'),
    path('location_application/', views.location_application, name='location_application'),
    path('datewise_application/', views.datewise_application, name='datewise_application'),
    path('export_dateexcel/', ExportExceldatewise.as_view(), name='export_dateexcel'),

]
