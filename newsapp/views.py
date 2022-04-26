from asyncio.windows_events import NULL
from datetime import date, datetime
import email
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from newsapp.form import AddReportForm, AdminLoginForm, RpLoginForm, UserRegisterForm
from newsapp.models import AdminLogin, RpLogin, AddReport
from django.core.mail import send_mail


# Create your views here.
def Index(request):
    return render(request, "admin/index.html")

def rIndex(request):
    return render(request, "user/reporter-index.html")

def AddNews(request):
    report = AddReportForm
    # it get the the status 0 or 1
    reporterverify = request.session['verified']
    return render(request, "user/addreport.html", {'form':report, 'reporterverify':reporterverify})    


def SaveNews(request):
    report = AddReportForm
    try:
    #image = request.POST.get("image")
        image = request.FILES['image']
        Date = date.today()
        Title = request.POST.get("Title")
        Description = request.POST.get("Description")
        Type = request.POST.get("Type")
        reporterusername = request.session['username'] #get reporter username for whom report is added

        # approvement for reporter
        approval = False
        

        new_report = AddReport(image=image, Date = Date, Title=Title, Description=Description, \
                               approval = approval, Type = Type, reporterid = reporterusername)
        new_report.save()
        msg = "New Report Added Successfully!!!!"
        return render(request, "user/addreport.html", {'form':report, 'msg':msg})
    except:
        msg = "Error!!!"
        return render(request, "user/addreport.html", {'form':report, 'msg':msg})     








def ShowAllNews(request):
    pending_news = AddReport.objects.filter(approval = False)
    return render(request, "admin/allnews.html", {'report':pending_news})   












def EditReport(request, note_id):
    edit = AddReport.objects.get(id=note_id)
    return render(request, "admin/editreport.html", {'edit':edit})


def update(request):
    note_id = request.POST.get('id')  
    try:
        edit = AddReport.objects.get(id=note_id)
        if request.FILES['image'] != NULL:
            edit.image = request.FILES['image']  
        else:
            edit.image = edit.image

        edit.Title = request.POST.get('title')
        edit.Description = request.POST.get('description')
        edit.save()
        msg = "successfully updated!!!"  
        all_report = AddReport.objects.all() 
        return render(request, "user/ReporterNews.html", {'msg':msg, 'report': all_report })

    except:
        msg = "Report update failed!!!"
        edit = AddReport.objects.get(id=note_id)
        return render(request, 'admin/editreport.html', {'edit':edit, 'msg':msg})   

def delete(request, note_id):
    data_report = AddReport.objects.get(id=note_id)
    data_report.delete()
    report = AddReport.objects.all()
    return render(request, 'user/ReporterNews.html', {'report':report})         




def AprroveNews(request, note_id):
    approve = AddReport.objects.get(id=note_id)
    approve.approval = True
    approve.save()
    all_report = AddReport.objects.filter(approval = False)
    return render(request, "admin/allnews.html", {'report': all_report })

    

#all approved news
def userNews(request):
    main = AddReport.objects.filter(Type="main", approval = True)
    sub = AddReport.objects.filter(Type="sub", approval = True)
    return render(request, 'alluser.html', {'main':main, 'sub':sub})


def singlePage(request, note_id):
    details = AddReport.objects.get(id=note_id)
    return render(request, 'singlepage.html',{'details':details} )



#admin
def adminLogin(request):
    loginform = AdminLoginForm
    return render(request,"admin/adminlogin.html",{'form':loginform})


def adminIndex(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    adminLoginForm = AdminLoginForm()
    try:
        user = AdminLogin.objects.get(username=username)
        if(password == user.password):
            request.session['username'] = username
            return render(request, "admin/index.html", {'username':username})
        else:
            msg = "Invalid Password"
            return render(request, "admin/adminlogin.html", {'form':adminLoginForm, 'msg':msg })
    except:
        msg = "Invalid username"
        return render(request, "admin/adminlogin.html", {'form':adminLoginForm, 'msg':msg })


#reporter
def reporterLogin(request):
    loginform = RpLoginForm
    return render(request,"user/reporterlogin.html",{'form':loginform})


def reporterIndex(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    loginform = RpLoginForm()
    try:
        user = RpLogin.objects.get(username=username)
        if(user.id_approve == True):
            if(password == user.password):
                request.session['id'] = user.id
                request.session['username'] = username
                request.session['verified'] = user.verified
                return render(request, "user/reporter-index.html", {'username':username})
            else:
                msg = "Invalid Password"
                return render(request, "user/reporterlogin.html", {'form':loginform, 'msg':msg })
        
        else:
            msg = "ID not approved yet"
            return render(request, "user/reporterlogin.html", {'form':loginform, 'msg':msg }) 

    except:
        msg = "Invalid username"
        return render(request, "user/reporterlogin.html", {'form':loginform, 'msg':msg })


def Logout(request):
    user_login = RpLoginForm()
    if request.session.has_key('username'):
            del request.session['username']
            return render(request, "user/reporterlogin.html",{'form' : user_login})
    else:
            return render(request, "user/reporterlogin.html",{'form' : user_login})



#reporter news 
def ReporterNews(request):
    username_id = request.session['username'] #as per id news filter by username
    report = AddReport.objects.filter(reporterid=username_id)
    return render(request, "user/ReporterNews.html", {'report':report} )   


#Reporter register
def register(request):
    reg_form = UserRegisterForm()
    return render(request, "user/register.html", {'form': reg_form}) 



def ReporterRegister(request):
    reg_form = UserRegisterForm()
    try:
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        image_url = request.FILES['image_url']

        # approvement for reporter
        id_approve = True

        # uname = RpLogin.objects.filter(username=username)

        new_report_acc = RpLogin(firstname=firstname, lastname = lastname, username=username, password = password, email = email, contact = contact, image_url = image_url, id_approve = id_approve )
        new_report_acc.save()
        msg = "User Registered Successfully"
        return render(request, "user/register.html", {'form': reg_form, 'msg' : msg})
        # else:
        #     msg = "Ivalid !!!!"
        #     return render(request, "register.html", {'form': reg_form, 'msg' : msg})

    except:
        msg = "Failed to register!!"
        return render(request, "user/register.html", {'form': reg_form, 'msg' : msg})


def ShowAllreporter(request):
    member = RpLogin.objects.filter(id_approve=False)
    return render(request, "admin/allmember.html", {'member':member})        


def yourProfile(request): 
    user_id = request.session['id']
    reporterverify = request.session['verified']
    user_details = RpLogin.objects.get(id=user_id)
    return render(request, "user/profile.html",{'data':user_details, 'reporterverify':reporterverify} )    

#new member approve
def memberAprrove(request, note_id):
    approve = RpLogin.objects.get(id=note_id)
    approve.id_approve = True
    approve.save()
    member = RpLogin.objects.all() 
    return render(request, "admin/allmember.html", {'member': member })

    
def EditProfile(request, note_id):
    edit = RpLogin.objects.get(id=note_id)
    return render(request, "user/editprofile.html", {'edit':edit})


def ProfileUpdate(request):
    note_id = request.POST.get('id')  
    try:
        edit = RpLogin.objects.get(id=note_id)  
        edit.firstname = request.POST.get('firstname')
        edit.lastname = request.POST.get('lastname')
        edit.contact = request.POST.get('contact')
        edit.image_url = request.FILES['image_url']
        edit.save()
        data = RpLogin.objects.all() 
        return render(request, "user/profile.html", {'data': data })

    except:
        msg = "profile update failed!!!"
        edit = RpLogin.objects.get(id=note_id)
        return render(request, 'user/editprofile.html', {'edit':edit, 'msg':msg}) 


# Admin approve email
def sendEmail(request, note_id):
    userid = RpLogin.objects.get(id=note_id)
    email = userid.email
    userid.id_approve = True
    userid.save()

    send_mail(
                subject = "account verified",
                message = "Congrats your reporter account has been verified successfully",
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [email],
                fail_silently = False,
                
        )
    member = RpLogin.objects.filter(id_approve = False)   
    return render (request, 'admin/allmember.html', {'member' : member})






#send email verification
def SendVerifyEmail(request):
    if request.method == "GET":
        email = request.GET.get('email', None)
        code = request.GET.get('code', None)
        send_mail(
            subject = 'OTP Email Verification',
            message = code + ' is your OTP verification code.',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [email],
            fail_silently = False,
            # fail_silently takes boolean value. If set False it will raise smtplib.STMPException if the error
            # occurs while sending the email
        )
        return JsonResponse({"success": "Success"}, status=200)
    else:
        return JsonResponse({"error": "form.errors"}, status=400)




# def pedingAcc(request):
#     pending = RpLogin.objects.filter(id_approve = False)
#     return render(request, 'admin/allmember.html', {'member':pending})

def verifiedAcc(request):
    approved = RpLogin.objects.filter(id_approve = True)
    return render(request, 'admin/verifieduser.html', {'member':approved})


def ApprovedNews(request):
    appv_news = AddReport.objects.filter(approval = True)
    return render(request, 'admin/approvednews.html', {'report':appv_news})




#user verification
def userExist(request):
    if request.method == "GET":
        username = request.GET.get('uName', None)
        data = RpLogin.objects.filter(username = username)
        if data.count() == 0:
            return JsonResponse({"message": "Success"}, status=200)
        else:
            return JsonResponse({"message": "Errors"}, status=200)
    else:
            return JsonResponse({"error": "form.errors"}, status=400)        




#status user verification
def updateVerifyStatus(request):
    try:
        verifystatus = request.session['id']
        rverified = RpLogin.objects.get(id=verifystatus)
        rverified.verified = True
        rverified.save()
        return JsonResponse({"message": "Success"}, status=200)
    except:
        return JsonResponse({"error": "form.errors"}, status=400)   