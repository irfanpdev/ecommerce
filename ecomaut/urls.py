
from django.urls import path,include
from ecomaut import views
from .views import account_verify,forgetpass_link_activate
urlpatterns = [
 
    path('signup/',views.signup,name="signup"),
    path('login',views.handlelogin,name="login"),
    path('logout/',views.handlelogout,name="logout"),
    path('account-verify/<slug:token>',account_verify,name='account_verify'),
    path('changePassword',views.changePassword,name='changePassword'),
    path('sendQuery',views.sendQuery,name='sendQuery'),
    path('forgetpasslink',views.forgetpasslink,name='forgetpasslink'),
    path('forgetpass_link_activate/<slug:forgetPasstoken>',forgetpass_link_activate,name='forgetpass_link_activate'),
    path('forgetpass',views.forgetpass,name='forgetpass'),
    
]
