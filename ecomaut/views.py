from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from .utils import *
from .models import Profile
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password

# Create your views here.
def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['passwd']
        cpasswd=request.POST['cpass']
       
        if password !=cpasswd:
            
            messages.error(request,'Password and confirm Password not matched')
            return render(request,'auth/signup.html')
        try:
            if User.objects.get(username=email):
            
                messages.info(request,'Email Id already exist')
                return render(request,'auth/signup.html')
        except Exception as indentifier:
            pass
       
       
        user_obj=User.objects.create_user(email, email, password,first_name=name)
        user_obj.save()
        uid=uuid.uuid4()
        p_obj=Profile(user=user_obj,token=str(uid))
        p_obj.save()
       
        send_email_token(email,p_obj.token)
        messages.success(request,'User created successfully. Check your email and click link to verify account')
        return render(request,'auth/login.html')
   
    return render(request,'auth/signup.html')

        
    #return render(request,'auth/signup.html')

def account_verify(request,token):
     try:
         
          obj=Profile.objects.filter(token=token).first()
          
          if obj.verify==True:
              messages.success(request,'Your account already verifed. You can now loing to your account')
              return render(request,'auth/login.html')
          else:  
            obj.verify=True
            obj.save()
            messages.success(request,'Your account verfify successfully. You can now loing to your account')
            return render(request,'auth/login.html')
     except Exception as e:
             messages.error(request,'Invalid token')

def check_emailId_exists(email):
    try:
        return User.objects.get(email=email)  
        
    except:
        return False

def verify_password(password):
    try:
         
         return check_password(password,password)
        
    except:
        return False

def handlelogin(request):
   
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['passwd']
        try:
            user = authenticate(request, username=str(username).lower(), password=password)
            if user is not None: 
                proobj=Profile.objects.get(user=user)
                if  proobj.verify==True:
                    login(request,user)
                    return redirect('/')
                else:
                    messages.success(request,'Your account is not active. Please verfify your account by clicking link in your email')  
                    return render(request,'auth/login.html')
              
            if check_emailId_exists(username)==False:
                messages.error(request,'Your Email Id does not exist')
                return render(request,'auth/signup.html')    
            
            if verify_password(password)==False:
                messages.error(request,'Wrong password')
                return render(request,'auth/login.html')
    
        except Exception as indentifier:
            return False  
    return render(request,'auth/login.html')

def changePassword(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            crpassword=request.POST['crpasswd']
            password=request.POST['passwd']
            rpass=request.POST['cpass']
            user=User.objects.get(id=request.user.id)
            check=user.check_password(crpassword)
            un=user.username
            if password !=rpass:
                messages.error(request,'Password and confirm Password not matched')
                return render(request,'auth/changepass.html')
            else:
                if check==True:
                    user.set_password(rpass)
                    user.save()
                    messages.success(request,'Your password has been changed successfully')
                    #logout(request)
                    #if want to user be loing after password change
                    user=User.objects.get(username=un)
                    login(request,user)
                    return redirect('/')
                    
                else:
                    messages.success(request,'Your current  password is incorrect')
                    return render(request,'auth/changepass.html')
    else:
        messages.success(request,'Login into your account to change password')
                    
        return render(request,'auth/login.html')
        

    return render(request,'auth/changepass.html')


def handlelogout(request):
    logout(request)
    messages.success(request,'You have succesfully loged out')
    return redirect('login')
   

def sendQuery(request):
    if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']
            subject=request.POST['subject']
            message=request.POST['message']
            email_from =settings.EMAIL_HOST_USER
            recipent_list=[settings.EMAIL_HOST_USER]
            msg=f'Name: {name} \n Email: {email} \n Message: {message}'
            send_mail(subject,msg,email_from,recipent_list)
            messages.success(request,'Your message has been sent. Thank you!')
            return redirect('sendQuery')
    return render(request,'contactus.html')

def forgetpasslink(request):
    try:
        if request.method=='POST':
            email=request.POST['email']
            user=User.objects.filter(username=email).first()
            if user is not None:
                uid=uuid.uuid4()
                token_obj=Profile.objects.get(user =user)
                token_obj.forgetPasstoken=uid
                token_obj.save()
                
                send_email_reset_token(email=user.username, forgetPasstoken=str(uid))
                messages.success(request,'Reset Password link sent to your email.')
                token_obj.fotgetPassLinkExpStatus=False
                token_obj.save()
            if user is None:
                messages.error(request,'Your Email Id does not exist')
                return render(request,'auth/signup.html')
        
    except Exception as indentifier:
            pass
    return render (request,'auth/forgetpasslink.html')

def forgetpass_link_activate(request,forgetPasstoken):
    try:
        pro_obj=Profile.objects.filter(forgetPasstoken=forgetPasstoken).first()
        if pro_obj.fotgetPassLinkExpStatus==False:
            user=User.objects.get(username=pro_obj.user)
            if user is not None:
                if pro_obj.forgetPasstoken==forgetPasstoken:
                    
                    return render(request,'auth/forgetpass.html',{'forgetPasstoken':forgetPasstoken})
                    
                
                else:
                    messages.error(request,'Invalid token')
        else:
            messages.error(request,'Link has been expried. Generate new link to reset password')
    except Exception as e:
     messages.error(request,'Link has been expried. Generate new link to reset password')
     return False
        
def forgetpass(request):

        
        forgetPasstoken=request.POST.get('forgetPasstoken')
        password=request.POST['passwd']
        rpass=request.POST['cpass']
       
        pobj=Profile.objects.filter(forgetPasstoken=forgetPasstoken).first()
        user=User.objects.filter(username=pobj.user).first()
      
       
        if password !=rpass:
            messages.error(request,'Password and confirm Password not matched')
            return render(request,'auth/forgetpass.html')
        else:
            
                user.set_password(rpass)
                user.save()
                pobj.fotgetPassLinkExpStatus=True
                pobj.save()
                messages.success(request,'Your password has been changed successfully')
                return render(request,'auth/login.html')
    
        


    
   