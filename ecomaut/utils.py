from django.conf import settings
from django.core.mail import send_mail

def send_email_token(email,token):
    try:
        subject = 'Your account need to be verified'
        message = f'Click on the link to verify https://ecommercesrv.onrender.com/ecomaut/account-verify/{token}'
        email_from =settings.EMAIL_HOST_USER
        recipent_list= [email]
        send_mail(subject,message,email_from,recipent_list)
    except Exception as e:
        return False
    return True

def send_email_reset_token(email,forgetPasstoken):
    try:
        subject = 'Reset Password'
        message = f'Click on the link to reset password https://ecommercesrv.onrender.com/ecomaut/forgetpass_link_activate/{forgetPasstoken}'
        email_from =settings.EMAIL_HOST_USER
        recipent_list= [email]
        send_mail(subject,message,email_from,recipent_list)
    except Exception as e:
        return False
    return True
