from django.urls import path
from.import views

urlpatterns = [
    path('parenthome', views.parenthome,name="parenthome"),
    path('admission', views.admission,name="admission"),
    path('admissiondetails/<id>', views.admissiondetails,name="admissiondetails"),
    path('application/<id>', views.application,name="application"),
    path('confirmdetails/', views.confirmdetails, name="confirmdetails"),
    path('viewmore/<id>', views.viewmore, name="viewmore"),
    path('payment/<id>', views.payment, name="payment"),
    path('progresskids', views.progresskids,name="progresskids"),
    path('progressdetails/<id>', views.progressdetails,name="progressdetails"),
    path('logout/', views.logout, name='logout'),
    path('parentprofile', views.parentprofile, name="parentprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/', views.changepassword, name="changepassword"),

]