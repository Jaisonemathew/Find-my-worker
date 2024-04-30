from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import booking , Worker
from .models import booking
from .models import feedback
from .models import notification
from .models import review
from .form import userUpdate



# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"invalid login details!")
            return redirect('/')
        return render(request,"login.html")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username Already Taken!")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email Already Taken!")
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
        return redirect('/')
    return render(request,"register.html")

def index(request):
   
    return render(request,"index.html")

from .models import Worker
def bookingf(request):
 
    
    obj=Worker.objects.all()
    print(obj)
    context={
'obj':obj,
    }
    return render(request,"booking.html",context)
    

def profile(request):

    return render(request,"profile.html")
   
from .models import booking
def details(request,worker):
    print(worker)
    if request.method == 'POST':
        user = request.user
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phno=request.POST['phno']
        address=request.POST['address']
        district=request.POST['district']
        amount=request.POST['amount']
        worker=worker
        messages.success(request, 'Booking successful and sent to admin for approval.')
        book=booking.objects.create(user=user.username,firstname=firstname,lastname=lastname,phno=phno,address=address,district=district,amount=amount,worker=worker)
        book.save()
      
        return redirect('mybookings')

    return render(request,"details.html",{'worker':worker})
  
def mybookings(request):
    user= request.user.username
    book=booking.objects.filter(user=user).all()
    print(book)
    context = {
        'userbooking':book
        }
    return render(request, 'mybookings.html',context)

  
def cancel(request,id):
    user= request.user.username
    item=booking.objects.get(id=id)
    item.delete()

    book=booking.objects.filter(user=user).all()
    context = {
        'userbooking':book
        }
    return render(request, 'mybookings.html',context)

    
def fdback(request):
    if request.method == 'POST':
        
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        message=request.POST['message']
        
        f = feedback.objects.create(name=name,phone=phone,email=email,message=message)
        print(f)
        f.save()
      
        return redirect("index")


def construction(request):
   
    return render(request,"construction.html")

def RECONSTRUCTION(request):
   
    return render(request,"RECONSTRUCTION.html")

def ELECTRICAL(request):
   
    return render(request,"ELECTRICAL.html")

def notify(request):

    if request.method == 'POST':
        
        email=request.POST['email']
        
        n = notification.objects.create(email=email)
        print(n)
        n.save()
      
        return redirect("index")

def Review(request):

    if request.method == 'POST':

        name=request.POST['name']
        message=request.POST['message']
        email=request.POST['email']

        rev=review.objects.create(name=name,message=message,email=email)
        rev.save()
      
        return redirect('seemore')

    return render(request,"review.html")

def smore(request):

    rev=review.objects.all()
    print(rev)
    context = {
        'rw':rev
        }

    return render(request,"seemore.html",context)


def update(request,id):
    update_element=User.objects.get(id=id)
    form=userUpdate(request.POST or None,instance=update_element)
    if form.is_valid():
        form.save()
        return redirect("profile")

    return render(request,'update.html',{'form':form,'id':id})
   

def client(request):
   
    return render(request,"client.html")

def award(request):
   
    return render(request,"award.html")

def trustable(request):
   
    return render(request,"trustable.html")

def creator(request):
   
    return render(request,"creator.html")
