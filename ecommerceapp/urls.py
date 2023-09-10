from django.conf import settings
from django.urls import path,include
from ecommerceapp import views
from django.conf.urls.static import static
urlpatterns = [
 
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('portfolio',views.portfolio,name="portfolio"),
    path('price',views.price,name="price"),
    path('team',views.team,name="team"),
    path('testomonial',views.testomonial,name="testomonial"),
    path('features',views.features,name="features"),
    path('contact',views.contact,name="contact"),
    path('getStarted',views.getStarted,name="getStarted"),
    path('show',views.show,name="show"),
    path('imgload',views.imgload,name='imgload')


]