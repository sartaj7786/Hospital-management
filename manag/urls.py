from django.urls import path
from manag import views

urlpatterns = [
    path('index/',views.index ,name="index"),
    path('about/',views.About ,name="about"),
    path('contact/',views.Add_Contact ,name="contact"),
    path('doctor/',views.Add_Doctor ,name="doctor"),
    path('patient/',views.Add_Patient ,name="patient"),
    path('',views.Signup ,name="signup"),
    path('login/',views.Login ,name="login"),
    path('logout/',views.Logout ,name="logout"),
]
