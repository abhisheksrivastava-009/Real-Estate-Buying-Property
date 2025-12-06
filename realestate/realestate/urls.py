"""
URL configuration for realestate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views import Home
from myapp.views import Contact_Info
from myapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("About",AboutUs),
    path('new',newpage),
    path('second',SecondPage),
    path('sec',Second),
    path('third',Third),
    path('reg',Register),
    path('regis',RegisterForm),
    path('rgform',RegForm),
    path('data',DataTABLE),
    path('show',ShowData),
    path('ho',NewPage),
    path('cont', Contact_Info, name='contact'),
    path('abt',AboutUS),
    path('abtus',About_Join_Us),
    path('abtac',About_actuion),
    path('hom',Home),
    path('home',Buyhouse),
    path('byflt',BuyFlat),
    path('byapp',BuyApartment),
    path('sell',SellHouse),
    path('sellft',SellFlat),
    path('login',LoginPage),
    path('pvc',PrivacyPolicy),
    path('sin',Signup),
    path('sh',ShowAllData),
    path('showall',showdataintable),
    path('Editpage/<int:eid>',EditPage),
    path('',NewRegForm),
    path('Log',NewLogin),path('userReg',NewRegForm),
    path ('lg',LOG),
    path ('ag',Agent1),
    path ('ag2',Agent2),
    path ('ag3',Agent3),
    path ('ag4',Agent4),
    path('cont_info', Contact_Info, name='contact_info'),
    # path('logout', Logout),

 
    path ('if',Innerform),
    path ('tc',Termcond),



    


]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
