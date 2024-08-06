from django.urls import path
from.import views

urlpatterns = [
    path('daycarehome', views.index,name="daycarehome"),
    path('applicationrequest', views.applicationrequest,name="applicationrequest"),
    path('applicationdetails/<id>', views.applicationdetails,name="applicationdetails"),
    path('confirmrequest/<id>', views.confirmrequest,name="confirmrequest"),
    path('rejectrequest/<id>', views.rejectrequest,name="rejectrequest"),
    path('applicationconfirmed', views.applicationconfirmed,name="applicationconfirmed"),
    path('appconfirmdetails/<id>', views.appconfirmdetails,name="appconfirmdetails"),
    path('progress', views.progress,name="progress"),
    path('deleteprogress/<id>', views.deleteprogress, name="deleteprogress"),
    path('logout/', views.logout, name='logout'),

]