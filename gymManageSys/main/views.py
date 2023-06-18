from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Count
from .import models
#from .models import displayusername
from .import forms
import stripe
import datetime

from datetime import timedelta

# Home Page
def home(request):
    banners=models.Banners.objects.all()
    services= models.Service.objects.all()[:3]
    gimgs=models.GalleryImage.objects.all().order_by('-id')[:9]
    return render(request, 'home.html',{'banners':banners,'services':services,'gimgs':gimgs})

#PageDetail
def page_detail(request, id):
    page=models.Page.objects.get(id=id)
    return render(request, 'page.html',{'page':page})

#FAQ
def faq_list(request):
    faq=models.Faq.objects.all()
    return render(request, 'faq.html',{'faqs':faq})
    
#Enquiry
def enquiry(request):
    msg = ''
    if request.method=='POST':
        form=forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            msg='Data has been saved'
    form = forms.EnquiryForm
    return render(request, 'enquiry.html',{'form':form, 'msg': msg})

# Show Galleries
def gallery(request):
    gallery=models.Gallery.objects.all().order_by('-id')
    return render(request, 'gallery.html',{'gallerys':gallery})

# Show Galleries photos
def gallery_detail(request, id):
    gallery=models.Gallery.objects.get(id=id)
    gallery_imgs=models.GalleryImage.objects.filter(gallery=gallery).order_by('-id')
    return render(request, 'gallery_imgs.html',{'gallery_imgs':gallery_imgs, 'gallery': gallery})
    
#Subscription Plan
def pricing(request):
    pricing=models.SubPlan.objects.annotate(total_members=Count('subscription__id')).all().order_by('price')
    dfeatures=models.SubPlanFeature.objects.all()
    dfeatures=models.SubPlanFeature.objects.all()
    return render(request, 'pricing.html',{'plans':pricing, 'dfeatures':dfeatures})

# SignUp
def signup(request):
    msg=None
    if request.method=='POST':
        form=forms.SignUp(request.POST)
        if form.is_valid():
            form.save()
            msg='thank you for register.'
    form= forms.SignUp
    return render(request, 'registration/signup.html',{'form':form, 'msg':msg})

#Checkout
def checkout(request, plan_id):
    plan=models.SubPlan.objects.get(pk=plan_id)
    reg_date=datetime.date.today()
    end_date=reg_date+timedelta(days=plan.validity_days)
    planDetail=models.SubPlan.objects.get(pk=plan_id)
    displaynames=User.objects.all()
    
    if request.method=="POST":
        models.Subscription.objects.create(
        plan=plan,
        user=User.objects.get(pk=request.POST.get('subscriptor')),
        price=plan.price,
        reg_date=reg_date,
        end_date=end_date
        )
        return redirect("pay_success")
        #user=User.objects.filter(username=request.POST.get('subscriptor'))
    return render(request, 'checkout.html',{'plan':planDetail,'displayusername':displaynames})
    #return render(request, 'checkout.html',{'plan':planDetail,'displayusername':displaynames})
    
stripe.api_key='sk_test_51NGrnoAfZJpIgEtviwMc8uPCgpkkTjiHLiVMQc4wskle0FVo96W2qmEJELarYq5FGiRgFyTOQuby237Imh9SZw0k00fP7daDGx'

def checkout_session(request,plan_id):
    plan=models.SubPlan.objects.get(pk=plan_id)
    request.session['plan']=plan
    request.session['plan_id']=plan_id
    #session=stripe.checkout.Session.create(
     #       payment_method_types=['card'],
      #      line_items=[
       #         {
        ##            'price_data': {
          #              'currency': 'inr',
           #             'product_data':{
            #                'name': plan.title,
             #           },
              #          'unit_amount': plan.price*100,
               #     },
                #    'quantity': 1,
                #},
            #],
            #mode='payment',
            #success_url='http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}',
            #cancel_url='http://127.0.0.1:8000/pay_cancel',
            #client_reference_id=plan_id
        #)
    
    return redirect("pay_success")

# Success


def pay_success(request,):
    #session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    #plan_id=request.session('plan_id')
    #plan=models.SubPlan.objects.get(pk=plan_id)
    #user=request.session.get('usuario')
    #reg_date=datetime.date.today()
    #models.Subscription.objects.create(
     #   plan=plan,
      #  user=user,
       # price=plan.price,
       # reg_date=reg_date,
       # end_date=reg_date+timedelta(days=plan.validity_days)
    #)
    #------ EMAIL DE ORDEN------
    
    message = 'Orden de compra de prueba 123'
    email = 'joeljaquez123@hotmail.com'
    name = 'No se que va aqui'
    send_mail(
        'Orden de compra',
        message,
        'joeljaqu123@gmail.com',
        [email],
        fail_silently=False)
    return render(request, 'success.html')
# Cancel
def pay_cancel(request):
    return render(request, 'cancel.html')

 # User Dashboard Section start
def user_dashboard(request):
    current_plan=models.Subscription.objects.filter(user=request.user).order_by('-id')[0]
    my_trainer=models.AssignSubscriber.objects.get(user=request.user)
    enddate=current_plan.reg_date+timedelta(days=current_plan.plan.validity_days)
    # notification detail
    data=models.Notify.objects.all().order_by('-id')
    notifStatus=False
    jsonData=[]
    totalUnread=0
    for d in data:  
        try:
            notifStatusData=models.NotifUserStatus.objects.get(user=request.user,notif=d)
            if notifStatusData:
                notifStatus=True
        except models.NotifUserStatus.DoesNotExist:
            notifStatus=False
        if not notifStatus:
            totalUnread=totalUnread+1    
    return render(request, 'user/dashboard.html',{
        'current_plan': current_plan,
        'my_trainer': my_trainer,
        'total_unread': totalUnread,
        'enddate': enddate

        })

#edit form
def update_profile(request):
    msg =None
    if request.method=='POST':
        form=forms.ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            msg='Data has been saved'
    form=forms.ProfileForm(instance=request.user)        
    return render(request, 'user/update-profile.html',{'form': form, 'msg': msg})

#Trainer login
def trainerlogin(request):
    msg = ''
    if request.method=='POST':
        username=request.POST['username']
        pwd=request.POST['pwd']
        trainer=models.Trainer.objects.filter(username=username,pwd=pwd).count()
        if trainer > 0:
            trainer=models.Trainer.objects.filter(username=username,pwd=pwd).first()
            request.session['trainerLogin']=True
            request.session['trainerid']=trainer.id
            return redirect('/trainer_dashboard')
        else:
            msg='Invalid!!'
    form = forms.TrainerLoginForm
    return render(request, 'trainer/login.html',{'form':form, 'msg': msg})

# Trainer Logout
def trainerlogout(request):
    del request.session['trainerLogin']
    return redirect('/trainerlogin')

# Trainer Dashboard
def trainer_dashboard(request):
    data=models.Notify.objects.all().order_by('-id')
    return render(request, 'trainer/dashboard.html',{'data': data})

# Trainer Profile
def trainer_profile(request):
    t_id=request.session['trainerid']
    trainer=models.Trainer.objects.get(id=t_id)
    msg=None
    if request.method=='POST':
        form=forms.TrainerProfileForm(request.POST,request.FILES,instance=trainer)
        if form.is_valid():
            form.save()
            msg='Profile has been update'
    form=forms.TrainerProfileForm(instance=trainer)
    return render(request, 'trainer/profile.html',{'form': form,'msg':msg})

# Notifications
def notifs(request):
    data=models.Notify.objects.all().order_by('-id')
    return render(request, 'notifs.html',{'data': data})

# Get all  Notifications
def get_notifs(request):
    data=models.Notify.objects.all().order_by('-id')
    notifStatus=False
    jsonData=[]
    totalUnread=0
    for d in data:  
        try:
            notifStatusData=models.NotifUserStatus.objects.get(user=request.user,notif=d)
            if notifStatusData:
                notifStatus=True
        except models.NotifUserStatus.DoesNotExist:
            notifStatus=False
        if not notifStatus:
            totalUnread=totalUnread+1    
        jsonData.append({
            'pk':d.id,
            'notify_detail': d.notify_detail,
            'notifStatus':notifStatus
        })
    return JsonResponse({'data': jsonData, 'totalUnread':totalUnread})

# Mark Read By User
def mark_read_notif(request):
    notif=request.GET['notif']
    notif=models.Notify.objects.get(pk=notif)
    user=request.user
    models.NotifUserStatus.objects.create(notif=notif,user=user, status=True)
    return JsonResponse({'bool': True})
    
# Trainer Subscribers
def trainer_subscribers(request):
    trainer=models.Trainer.objects.get(pk=request.session['trainerid'])
    trainer_subs= models.AssignSubscriber.objects.filter(trainer=trainer).order_by('-id')
    return render(request, 'trainer/trainer_subscribers.html',{'trainer_subs':trainer_subs})

# Trainer payments
def trainer_payments(request):
    trainer=models.Trainer.objects.get(pk=request.session['trainerid'])
    trainer_pays= models.TrainerSalary.objects.filter(trainer=trainer).order_by('-id')
    return render(request, 'trainer/trainer_payments.html',{'trainer_pays':trainer_pays})

# Trainer Change Password

def trainer_changepassword(request):
    msg= None
    trainer=models.Trainer.objects.get(pk=request.session['trainerid'])
    if request.method=='POST':
        new_password= request.POST['new_password']
        updateRes=models.Trainer.objects.filter(pk=request.session['trainerid']).update(pwd=new_password)
        if updateRes:
            del request.session['trainerLogin']
            return redirect('/trainerlogin')
        else:
            msg='Something is wrong!!'    
    form=forms.TrainerChangePassword
    return render(request, 'trainer/trainer_changepassword.html',{'form':form, 'msg':msg})

    # Trainer Notifications
def trainer_notifs(request):
    data=models.TrainerNotification.objects.all().order_by('-id')
    return render(request, 'trainer/notifs.html',{'notifs':data})

   # Trainer Messages
def trainer_msgs(request):
    data=models.TrainerMsg.objects.all().order_by('-id')
    return render(request, 'trainer/msgs.html',{'msgs':data})

   # Attandance
def attendance(request):
    current_plan=models.Subscription.objects.get(user=request.user)
    user=request.user
    context={
        'plan': current_plan,
        'usuario': user
    }
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    SelectTrainer=models.Trainer.objects.all()   
    if request.method=="POST":
        user=request.user
        Login=request.POST.get('logintime')
        Logout=request.POST.get('loginout')
        SelectWorkout=request.POST.get('workout')
        img=models.Subscriber.objects.get(user=request.user)
        query=models.Attendance(user=user,Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,img=img)
        query.save()
        messages.warning(request,"Attendace Applied Success")
        return redirect('/attendance')
    return render(request,"attendance.html",context)

class ChangePassword(LoginRequiredMixin,TemplateView):

    def get(self, request, *args, **kwargs):
        form_class = forms.MyPasswordChangeForm
        form = self.form_class(self.request.user)
        return render(request, 'password.html',{'form': form,})


