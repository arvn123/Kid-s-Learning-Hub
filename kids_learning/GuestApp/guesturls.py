from django.urls import path
from.import views

urlpatterns = [
    path('', views.index,name="index"),
    path('login/', views.loginnew, name="login"),
    path('parent/', views.parent, name="parent"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword")

]
