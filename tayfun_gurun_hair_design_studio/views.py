from django.shortcuts import render,redirect
from tayfun_gurun_hair_design_studio.models import Service,Order,Customer
from datetime import datetime
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.core.mail import send_mass_mail


def error_404(request):
  
    return render(request,"404.html")



def index(request):
    
    all_service=Service.objects.all()
    context={
        "all_service":all_service
    }
    return render(request,"index.html",context)


mail_sit=""
def randevu(request):
    
    if request.method =="GET":
        return redirect("/")

    else:
        name=request.POST.get("name")
        surname=request.POST.get("surname") 
        mail=request.POST.get("email") 
        phone=request.POST.get("phone") 
        message=request.POST.get("randevu_hour_selected")
        date=datetime.now() 
        if(len(name)>2 and len(surname)>2 and len(phone)>9):
                msj="Randevunuz başarıyla alınmıştır.Bizi tercih ettiğiniz için teşekkürler "+name+" "+surname
              
                newOrder=Order(first_name=name,last_name=surname,mail=mail,date=date, phone_number=phone,message=message)
                newOrder.save()

                try:
                    send_mail("Tayfun Gürün Hair Design Stüdio-Randevu",msj,"tayfungurunhairdesignstudio@gmail.com",[mail], fail_silently=False)
                    mail_sit="Randevunuz alındığına dair mail yollanmıştır."
                except:
                    mail_sit="Mail sisteminde bir problem olduğundan mail yollayamadık.Randevunuz Alınmışt."

                if(Order.objects.filter(first_name=name, last_name=surname,mail=mail,date=date).exists()):
                         
                       return redirect("/randevu_succ")
                else:
                       return redirect("/randevu_fail")
                if not Customer.objects.filter(phone_number = phone).exists():
                  newCustomer=Customer(first_name=name,last_name=surname,mail=mail,phone_number=phone,mail_sended="No")
                  newCustomer.save()

        return redirect("/randevu_fail")


def randevu_succ(request):

     context={
       "mail_sit":mail_sit
     }
     return render(request,"order_succ.html",context)

def randevu_fail(request):
     context={
            "mail_sit":mail_sit
          }
     return render(request,"randevu_fail.html",context)



def manage(request):
    
  all_order=Order.objects.all()
  all_service=Service.objects.all()
  all_customer=Customer.objects.all()

  context={
        "all_order":all_order,
        "all_service":all_service,
        "all_customer":all_customer
    }
  
  if request.user.is_authenticated:
    return render(request,"manage.html",context)
  else:
   
    return redirect("/")




def login(request):
    username = request.POST.get('name', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        dj_login(request, user)
        return redirect("/manage")
        
    else:
            return render(request,"login.html")





def log_out(request):
     logout(request)
     return redirect("/")


def send(request):
  
  mail_list=Customer.objects.only('mail')
  header = request.GET['mail_head']
  header_ex =request.GET['mail_ex']

  if request.user.is_authenticated:
        
          mails = [ recipient.mail for recipient in mail_list if recipient.mail_sended=="no" ]
          
          for mail in mails:
             try:
                    send_mail("Tayfun Gürün Hair Design Stüdio-Randevu",msj,"tayfungurunhairdesignstudio@gmail.com",[mail], fail_silently=False)
                    Customerupdate=Customer(mail=mail)
                    Customerupdate.save()
             except:
               print("mail yollarken bir sorun oluştu...")
            #message = 'test message'
            #from_email = 'tayfungurunhairdesignstudio@gmail.com'
            #messages = [(i, header_ex, from_email, [recipient.mail]) for recipient in mail_list]
            #send_mass_mail(messages)
     
          return redirect("/manage")

  else:
        return redirect("/")


def price_update(request):
  price_code = request.GET['price_code']
  new_price=request.GET['new_price']

  if(Service.objects.filter(id=price_code).exists()):

        service=Service.objects.get(id=price_code)
        service.price=new_price
        service.save()

  if request.user.is_authenticated:

        print( new_price)
        return redirect("/manage")
  else:
        return redirect("/")



def add_order(request):
        name=request.GET["name"]
        surname=request.GET["surname"]
        mail=request.GET["email"] 
        phone=request.GET["phone"]
        message=request.GET["message"]
        date=datetime.now() 
        if(len(name)>2 and len(surname)>2 and len(phone)>9):

                newOrder=Order(first_name=name,last_name=surname,mail=mail,date=date, phone_number=phone,message=message)
                newOrder.save()
                msj="Randevunuz başarıyla alınmıştır.Bizi tercih ettiğiniz için teşekkürler "+name+" "+surname

                try:
                    send_mail("Tayfun Gürün Hair Design Stüdio-Randevu",msj,"tayfungurunhairdesignstudio@gmail.com",[mail], fail_silently=False)
                    mail_sit="Randevunuz alındığına dair mail yollanmıştır."
                except:
                    mail_sit="Mail sisteminde bir problem olduğundan mail yollayamadık.Randevunuz Alınmışt."

          
        return redirect("/manage")


