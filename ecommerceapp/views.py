from django.shortcuts import render,HttpResponse
from .models  import *
import pathlib
from django.contrib import messages
from math import ceil

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


def services(request):
    return render(request,"services.html")

def portfolio(request):
    products=ImageUpload.objects.filter(imgType='WEB').all()
    products1=ImageUpload.objects.filter(imgType='APP').all()
    products2=ImageUpload.objects.filter(imgType='CARD').all()
    itm={'products':products,'products1':products1,'products2':products2}
    return render(request,"portfolio.html",itm)

def price(request):
    return render(request,"pricing.html")

def team(request):
    team=Team.objects.all()
    
    itm={'team':team}
    return render(request,"team.html",itm)
    

def testomonial(request):
    return render(request,"testomonial.html")

def features(request):
    return render(request,"features.html")

def contact(request):
    return render(request,"contactus.html")

def getStarted(request):
    return render(request,'indexcopy.html')



def imgload(request):
    if request.method=='POST':
        img=request.FILES.getlist('imgurl')
        imgType=request.POST['imgtype']
        strtouper=str(imgType).upper()
        #file_extension = pathlib.Path(str(img)).suffix
        FileExtensionlist=['.png','.jpg','.jpeg']
        
        #if any(FileExtensionlist, img):
        for img1 in img:
                
                newimg=ImageUpload.objects.create(img=img1,imgType=strtouper)
        messages.success(request,'Your file has been uploaded successfully')
        return render(request,"imgloading.html")
        #else:
         #   messages.error(request,'Your have selected invalid file type')
          #  return render(request,"imgloading.html")
        
    else:
        return render(request,'imgloading.html')
        

def show(request):
    #products=ImageUpload.objects.all()
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslide=n//4 + ceil((n/4)- (n//4))
        allprods.append([prod,range(1,nslide),nslide])
    params={'allprods':allprods}

    
    # products=ImageUpload.objects.filter(imgType='WEB').all()
    # products1=ImageUpload.objects.filter(imgType='APP').all()
    # products2=ImageUpload.objects.filter(imgType='CARD').all()
    # itm={'products':products,'products1':products1,'products2':products2}
    return render(request,'cart.html',params)



# static method
@staticmethod
def get_all_products():
    return Product.objects.all()

@staticmethod
def get_all_product_by_id(product_id):
    if product_id:
        return Product.objects.filter(category=product_id)
    else:
        return get_all_products()
