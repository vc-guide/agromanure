from django.shortcuts import render,redirect
from .models import products
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order_details
import decimal

# Create your views here.
def loginview(request):
  uname=request.POST['username']
  pwd=request.POST['password']
  user=authenticate(request,username=uname,password=pwd)
  if user is not None:
    login(request,user)
    return redirect('home')
  else:
    return render(request,"login.html")
  
def signup(request):
  uform=UserCreationForm(request.POST)
  if request.method=="POST":
    if uform.is_valid():
      uname=uform.cleaned_data.get('username')
      pwd=uform.cleaned_data.get('password1')
      email = request.POST["email"]
      user1=User.objects.create_user(username=uname,email=email,password=pwd)
      user1.save()
      user=authenticate(request,username=uname,password=pwd)
      login(request,user)
      return redirect('home')
  else:
    form1=UserCreationForm
    return render(request,'registration/sign_up.html',{'form':form1})
  return render(request,'registration/sign_up.html',{'form':uform})  


@login_required
def home(request):
  return render(request,"home.html")
def about(request):
  return render(request,"About.html")

def product_details(request):
  res={}
  try:
    prodtls=products.objects.all()
    res["pro"]=prodtls
    return render(request,"Products.html",res)
  except:
    return messages.error(request,"nothing finded")

def logout_view(request):
  logout(request)
  print('hello')
  return redirect('home')

def productview(request,product_name):
  if products.objects.filter(pro_name=product_name):
    product=products.objects.filter(pro_name=product_name).first
    context={'product':product}
  
  else:
    messages.error(request,"No such Category found")
    return redirect('Products')
  return render(request,"view.html",context)

'''def collect_order(request):
  if request.method=='POST':
    form=orderInfo(request.POST)
    if form.is_valid():
      form.save()
      return redirect('success')
    else:
      form=orderInfo()
      return render(request,'view.html',{'form':form})'''
def collect_order(request):
  d={}
  N=request.POST['name']
  A=request.POST['address']
  ph=request.POST['phone']
  pi=request.POST['pincode']
  pr_id=request.POST['pro_id']
  pr_name=request.POST['pro_nm']
  pr_price=decimal.Decimal(request.POST['pro_pr'])
  quant=request.POST['qt']
  imgurl=request.POST['img']
  tcost=decimal.Decimal(request.POST['tc'])   
  if len(ph)>=10 and len(pi)<=6:
    try:
      order=Order_details(username=request.user.username,Name=N,Address=A,phoneNo=ph,pincode=pi,product_id=pr_id,product_name=pr_name,quantity=quant,priceperunit=pr_price,totalprice=tcost,product_imgurl=imgurl)
      order.save()
      d={"p_img":imgurl,"p_name":pr_name,"p_q":quant,"p_tp":tcost,"p_address":A,"p_ph":ph,"msg":"Ordered Successfully"}
      print(d)
      return render(request,"success.html",d)
    except Exception as e:
      print(e)
      d["msg"]="error occurede"
      return render(request,"error.html",d)

  else:
    d["msg"]="Enter correct credentials"
    product=products.objects.filter(pro_name=pr_name).first
    context={'product':product}
  
    return render(request,"error.html",{'context':context,'d':d})
 
def orders(request):
  res={}
  order=Order_details.objects.filter(username=request.user.username)  
  res["ord"]=order
  return render(request,"vieworders.html",res)

def eventview(request):
  return render(request,"events.html")
def contactview(request):
  return render(request,"contact.html")


