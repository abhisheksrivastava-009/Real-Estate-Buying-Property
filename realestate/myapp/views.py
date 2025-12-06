from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import EmployeeData
from myapp.models import EmployeeData2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import ContactInfo
# Create your views here.
@login_required(login_url='lg')
def Home(request):
      return HttpResponse("Home Page")

def AboutUs(request):
      msg = "<h1 align='center'>About Us Page</h1>"
      return HttpResponse("AboutUs") 

def HomePage(request):
      return render(request,'HOMEPAGE.html')

def  newpage(request):
      return render(request,'newpage.html')

def nav(request):
      return render(request,'nav.html')

def SecondPage(request):
      context = {'user name': "sachin", "email":'sachin@gmail.com'}
      return render(request,'SecondPage.html', context)

def Second(request):
      context={'User Name': "amit","email":'amit@gmail.com'}
      return render(request,'Second.html',context)
def Third(request):
      return render(request,'Third.html')

def Register(request):
      if request.method=="POST" and 'subBtn1'in request.POST:
           print("Button 1 Clicked....",request.POST) 
           print("Welcome,request.POST['unm']")
     # print("Password",request.POST['PWD'])
      elif request.method=="POST" and 'subBtn2'in request.POST:
          print("Button 2 Clicked....",request.POST)

      return render(request,'Register.html')

def DataTABLE(request):
            if request.method=="POST" and 'RegBtn'in request.POST:
                  user = EmployeeData(
                        emp_name=request.POST.get('unm'),
                        emp_pwd=request.POST.get('pwd'),
                        emp_email=request.POST.get('mailID'),
                        emp_dob=request.POST.get('dob'),
                        emp_img=request.FILES.get('img_upd')

                  )
                  user.save()       
            return render(request,'DataTable.html')

def ShowData(request):
      return render(request,'ShowData.html')

def RegisterForm(request):
      return render(request,'RegisterForm.html')



def RegForm(request):
            print('hello')
            if request.method=="POST" and 'RegBtn'in request.POST:
                  # print('hello')
                  user = EmployeeData(
                        emp_name=request.POST.get('unm'),
                        emp_pwd=request.POST.get('pwd'),
                        emp_email=request.POST.get('mail_id'),
                        emp_mob=request.POST.get('mob_no'),
                        emp_dept=request.POST.get('dept'),
                        emp_dob=request.POST.get('dob'),
                        emp_img=request.FILES.get('img_upd')

                  )
                  user.save()       
            return render(request,'RegForm.html')


def Contact_Us(request):
    # helpful debug prints — remove later
    print("Contact_Us called, method:", request.method)
    if request.method == "POST" and 'RegBtn' in request.POST:
        fname = request.POST.get('unm')
        lname = request.POST.get('lnm')
        email = request.POST.get('mail_id')
        mob = request.POST.get('mob_no')
        ask = request.POST.get('ask')

        print("Received:", fname, lname, email, mob, ask)

        # create and save
        EmployeeData2.objects.create(
            emp_first_name=fname,
            emp_last_name=lname,
            emp_email=email,
            emp_mob=mob,
            emp_queire=ask
        )
        # optional: redirect to avoid double-submit on reload
        return HttpResponseRedirect('/cont')  

    return render(request, 'Contact_Us.html')


def ShowAllData(request):
      userData=None
      if request.method=="POST" and  'showBtn' in request.POST:
            userData = EmployeeData.objects.all().values()
      return render(request,"ShowAllData.html",{'userData':userData})

def EditPage(request,eid):
    if request.method=="POST" and  'subBtn3' in request.POST:
      userData = EmployeeData.objects.get(id=eid)
      userData.emp_pwd=  request.POSST.get('pwd') 
      userData.save()
      return HttpResponseRedirect('/show')
    userData =EmployeeData.objects.get(id=eid)
    return render(request ,"EditPage.html",{'userData': userData})

def showdataintable(request):
      if request.method=="POST" and  'showBtn' in request.POST:
            userData = EmployeeData.objects.all().values()
            print(userData)
            return render(request,"showdataintable.html",{'data':userData})

      return render(request,"showdataintable.html")

def NewRegForm(request):
      print("qwerty")
      if request.method=='POST' and 'logiBtn' in request.POST:
            unm = request.POST.get('unm')
            pwd = request.POST.get('pwd')
            user = authenticate(request,username=unm,password=pwd)
            print("qwerty",user)
            if user is not None:
                  login(request,user)
                  return HttpResponseRedirect('/hom')
            
      return render(request,"NewRegForm.html")

def NewLogin(request):
      if request.method=='POST' and 'regBtn' in request.POST:
            pwd = request.POST.get('pwd')
            rpwd = request.POST.get('retype_pwd')
            if pwd ==rpwd:
                User=User.objects.create_user(
                   username=request.POST.get('unm'),
                   email = request.POST.get('mail_id'),
                   password= request.POST.get('pwd'),
                  )
            user.save()        
      return render(request,"NewLogin.html")

@login_required(login_url='/login')
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

      





def NewPage(request):
      return render(request,'NewPage.html')
# def Contact_Us(request):
#       return render(request,'Contact_Us.html')
def AboutUS(request):
      return render(request,'AboutUS.html')
def About_Join_Us(request):
      return render(request,'About_Join_Us.html')
def About_actuion(request):
      return render(request,'About_actuion.html')
def Home(request):
      return render(request,'Home.html')
def Buyhouse(request):
      return render(request,'Buyhouse.html')
def BuyFlat(request):
      return render(request,'BuyFlat.html')
def BuyApartment(request):
      return render(request,'BuyApartment.html')

def SellHouse(request):
      return render(request,'SellHouse.html')
def SellFlat(request):
      return render(request,'SellFlat.html')
def LoginPage(request):
      return render(request,'LoginPage.html')
def PrivacyPolicy(request):
      return render(request,'PrivacyPolicy.html')
def Agent1(request):
      return render(request,'Agent1.html')
def Agent2(request):
      return render(request,'Agent2.html')
def Agent3(request):
      return render(request,'Agent3.html')
def Agent4(request):
      return render(request,'Agent4.html')
def Innerform(request):
      return render(request,'Innerform.html')
def Termcond(request):
      return render(request,'Termcond.html')

def Signup(request):
      if request.method=='POST' and 'regBtn' in request.POST:
            username = request.POST.get('unm')
            password = request.POST.get('pwd')
            email = request.POST.get('mail_id')
            
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                  return render(request, 'Signup.html', {'error': 'Username already exists'})
            
            # Check if email already exists
            if User.objects.filter(email=email).exists():
                  return render(request, 'Signup.html', {'error': 'Email already exists'})
            
            if username and password:  # Make sure username and password are not empty
                  try:
                        user = User.objects.create_user(
                              username=username,
                              password=password,
                              email=email
                        )
                        user.save()
                        # Automatically log the user in after signup
                        login(request, user)
                        return HttpResponseRedirect('hom')  # Redirect to home page after successful signup
                  except Exception as e:
                        return render(request, 'Signup.html', {'error': str(e)})
            else:
                  return render(request, 'Signup.html', {'error': 'Username and password are required'})
      
      return render(request, 'Signup.html')

def LOG(request):
      error = None
      if request.method == 'POST' and 'loginBtn' in request.POST:
            # The login form submits email as 'mail_id' in the template.
            identifier = request.POST.get('mail_id') or request.POST.get('unm')
            pwd = request.POST.get('pwd')

            user_obj = None
            # Try to find a user by email first (if user entered email), otherwise by username
            if identifier:
                  if '@' in identifier:
                        try:
                              user_obj = User.objects.get(email=identifier)
                        except User.DoesNotExist:
                              user_obj = None
                  else:
                        try:
                              user_obj = User.objects.get(username=identifier)
                        except User.DoesNotExist:
                              user_obj = None

            # If we found a matching user object, authenticate using their username
            if user_obj is not None:
                  user = authenticate(request, username=user_obj.username, password=pwd)
                  if user is not None:
                        login(request, user)
                        return HttpResponseRedirect('/hom')

            # If we reach here login failed
            error = 'Invalid username/email or password'

      return render(request, 'LOG.html', {'error': error})


# def search_property(request):
#     property_type = request.GET.get("type")

#     if property_type == "flat":
#         return redirect("/byflt/")
#     elif property_type == "house":
#         return redirect("/home/")
#     elif property_type == "apartment":
#         return redirect("/byapp/")
#     else:
#         return redirect("/")

def Contact_Info(request):
    if request.method == "POST" and 'submitBtn' in request.POST:
        # get data from form
        fname = request.POST.get('unm')
        lname = request.POST.get('lnm')
        email = request.POST.get('mail_id')
        mob = request.POST.get('mob_no')
        ask = request.POST.get('ask')

        # save to database
        ContactInfo.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            mobile=mob,
            query=ask
        )

        return HttpResponseRedirect('/cont_info')  # redirect to same page to avoid resubmit

    # fetch all existing entries
    all_contacts = ContactInfo.objects.all().order_by('-id')  # latest first

    return render(request, 'Contact_Info.html', {'all_contacts': all_contacts})

