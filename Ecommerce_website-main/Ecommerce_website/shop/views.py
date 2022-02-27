# view.py/shop


import json
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, OrderUpdate, Orders, Product
from math import ceil
# Create your views here.
def index(request):
    # products= Product.objects.all()
    # n =len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params= {'no_slide':nSlides, 'range':range(1,nSlides), 'product':products}
     
    allProds=[]
    catprods=Product.objects.values('category', 'id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n =len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4)) 
        allProds.append([prod, range(1,nSlides), nSlides])
        
    params={'allProds':allProds}
    return render(request, 'shop/index.html', params)

def searchFunc(query, item):
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.category.lower():
        return True
    else:
        return False
def search(request):
    query=request.GET.get('search').lower()
    allProds=[]
    catprods=Product.objects.values('category', 'id')
    cats={item['category'] for item in catprods}
    params={}
    for cat in cats:
        tempProd=Product.objects.filter(category=cat)
        prod=[item for item in tempProd if searchFunc(query, item)]
        n =len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        if len(prod)!=0:
            allProds.append([prod, range(1,nSlides), nSlides])
    params={'allProds':allProds, 'noResult':False}
    if len(allProds)==0:
        params['noResult']=True
    return render(request, 'shop/search.html', params)


def about(request): 
    return render(request, 'shop/about.html')

def contactUs(request):
    if request.method=='POST':
        name=request.POST.get('name', '')       
        email=request.POST.get('email', '')        
        phone=request.POST.get('phone', '')        
        desc=request.POST.get('desc', '')   
        contact=Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method=='POST':
        email=request.POST.get('email', '')
        orderId=request.POST.get('orderId', '')
        try:
            order=Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                updt=OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in updt:
                    updates.append({'text':item.update_desc, 'time':item.timeStamp})
                    response=json.dumps({'status':'success', "updates":updates, 'orderJson':order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noItem"}')  
        except:
            return HttpResponse('{"status":"error"}')  
        
    return render(request, 'shop/tracker.html')

def productView(request, myId):
    # Fetch the product using the ID
    product=Product.objects.filter(id=myId)
    return render(request, 'shop/productView.html', {'product':product[0]})



def checkout(request):
    if request.method=='POST':
        name=request.POST.get('name', '')        
        items_json=request.POST.get('items_json', '')        
        amount=int(request.POST.get('amount', ''))        
        email=request.POST.get('email', '')        
        phone=request.POST.get('phone', '')        
        address=request.POST.get('address1', '') + request.POST.get('address1', '')
        state=request.POST.get('state', '')        
        zip_code=request.POST.get('zip_code', '')        
        order=Orders(name=name, email=email, phone=phone, address=address,amount=amount, items_json=items_json, state=state, zip_code=zip_code)
        order.save()
        id=order.order_id
        print(id)
        updte=OrderUpdate(order_id=id, update_desc="Order has been placed" )
        updte.save()
        thank=True
        return render(request, 'shop/checkout.html',{'thank':thank, 'order_id':id})
    return render(request, 'shop/checkout.html')

def cartPage(request):
    return render(request, 'shop/cartPage.html')
    