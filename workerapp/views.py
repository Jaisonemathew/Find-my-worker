from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import booking , Worker,Customer,feedback,notification,review
from .form import userUpdate,customerForm,customerAddForm,workerForm,workerAddForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            try:
                if Customer.objects.filter(customer=user).exists():
                    return redirect('index')
                elif Worker.objects.filter(worker=user).exists():
                    return redirect('worker_dashboard')
                else:
                    messages.info(request, "User type is not recognized.")
                    return redirect('/')
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return redirect('/')
        else:
            messages.info(request, "Invalid login details!")
            return redirect('/')
    
    return render(request, "login.html")

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
        email=request.POST['email']
        address=request.POST['address']
        district=request.POST['district']
        amount=request.POST['amount']
        worker=worker
        messages.success(request, 'Booking successful waiting for confirmation.')
        book=booking.objects.create(user=user.username,firstname=firstname,lastname=lastname,phno=phno,email=email,address=address,district=district,amount=amount,worker=worker)
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

  
def cancel(request, id):
    user = request.user.username
    item = booking.objects.get(id=id)
    item.is_cancelled = True
    item.save()

    book = booking.objects.filter(user=user).all()
    context = {
        'userbooking': book
    }
    return render(request, 'mybookings.html', context)

    
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

def registerCustomer(request):
    registered = False
    if request.method == 'POST':
        var_customerForm = customerForm(request.POST)
        var_customerAddForm = customerAddForm(request.POST)
        if var_customerForm.is_valid() and var_customerAddForm.is_valid():
            customerprimary = var_customerForm.save()
            customerprimary.set_password(customerprimary.password)
            customerprimary.save()
            customerAdd = var_customerAddForm.save(commit=False)
            customerAdd.customer = customerprimary
            customerAdd.save()
            registered = True
    else:
        var_customerForm = customerForm()
        var_customerAddForm = customerAddForm()
    return render(request, 'registerCustomer.html', {'var_customerForm': var_customerForm, 'var_customerAddForm': var_customerAddForm, 'registered': registered})

def registerWorker(request):
    registered = False
    if request.method == 'POST':
        var_workerForm = workerForm(request.POST, request.FILES)
        var_workerAddForm = workerAddForm(request.POST, request.FILES)
        if var_workerForm.is_valid() and var_workerAddForm.is_valid():
            workerprimary = var_workerForm.save()
            workerprimary.set_password(workerprimary.password)
            workerprimary.save()
            workerAdd = var_workerAddForm.save(commit=False)
            workerAdd.worker = workerprimary
            if 'img' in request.FILES:
                workerAdd.img = request.FILES['img']
            workerAdd.save()
            registered = True
    else:
        var_workerForm = workerForm()
        var_workerAddForm = workerAddForm()
    return render(request, 'registerWorker.html', {
        'var_workerForm': var_workerForm,
        'var_workerAddForm': var_workerAddForm,
        'registered': registered
    })

def worker_dashboard(request):
    return render(request,"workerdash.html")
