from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,CreateView,DetailView,ListView,DeleteView,UpdateView
from django.contrib.auth import authenticate,login,logout
from wwapp.forms import User,UserRrgisterForm,CarBookingForm,UserLoginForm,CarEditForm,UserPersonalInfoForm,BlogForm,UserMessageForm,LocationForm
from django.contrib import messages
from wwapp.models import CarCategory,CarBooking,UserPersonalInfo,BlogModels,UserMessagesModel,LocationsModel
from django.urls import reverse_lazy
from django.core.mail import send_mail,settings

# from wwproject.settings import API_KEY,SECRET_API_KEY
# # # Create your views here.

# #razor pay integration
# razorpay_client = razorpay.Client(
#     auth=(API_KEY, SECRET_API_KEY))

# def homepage(request):
#     currency = 'INR'
#     amount = 20000  # Rs. 200
 
#     # Create a Razorpay Order
#     razorpay_order = razorpay_client.order.create(dict(amount=amount,
#                                                        currency=currency,
#                                                        payment_capture='0'))
 
#     # order id of newly created order.
#     razorpay_order_id = razorpay_order['id']
#     callback_url = 'paymenthandler/'
 
#     # we need to pass these details to frontend.
#     context = {}
#     context['razorpay_order_id'] = razorpay_order_id
#     context['razorpay_merchant_key'] = API_KEY
#     context['razorpay_amount'] = amount
#     context['currency'] = currency
#     context['callback_url'] = callback_url
 
#     return render(request, 'payment.html', context=context)

# def paymenthandler(request):
 
#     # only accept POST request.
#     if request.method == "POST":
#         try:
           
#             # get the required parameters from post request.
#             payment_id = request.POST.get('razorpay_payment_id', '')
#             razorpay_order_id = request.POST.get('razorpay_order_id', '')
#             signature = request.POST.get('razorpay_signature', '')
#             params_dict = {
#                 'razorpay_order_id': razorpay_order_id,
#                 'razorpay_payment_id': payment_id,
#                 'razorpay_signature': signature
#             }
 
#             # verify the payment signature.
#             result = razorpay_client.utility.verify_payment_signature(
#                 params_dict)
#             if result is not None:
#                 amount = 20000  # Rs. 200
#                 try:
 
#                     # capture the payemt
#                     razorpay_client.payment.capture(payment_id, amount)
 
#                     # render success page on successful caputre of payment
#                     return render(request, 'paymentsuccess.html')
#                 except:
 
#                     # if there is an error while capturing payment.
#                     return render(request, 'paymentfail.html')
#             else:
 
#                 # if signature verification fails.
#                 return render(request, 'paymentfail.html')
#         except:
 
#             # if we don't find the required parameters in POST data
#             return HttpResponseBadRequest()
#     else:
#        # if other than POST request is made.
#         return HttpResponseBadRequest()
class AccessHome(TemplateView):
    template_name='access_home.html'
    
class UserRegister(CreateView):
    template_name='user_register.html'
    model=User
    form_class=UserRrgisterForm
    
    def form_valid(self, form):
        User.objects.create_user(**form.cleaned_data)
        return redirect('enter_home')
    
class Adminlogin(View):
    def get(self,request,*args, **kwargs):
       form=UserLoginForm()
       return render(request,'adminlogin.html',{'form':form})

    def post(self,request,*args, **kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user.is_superuser==1:
            login(request,user)
            return render(request,'admin_panel.html')
        elif user:
            login(request,user)
            return render(request,'user_index.html')
        else:
            form=UserLoginForm()
            return render(request,'adminlogin.html',{'form':form})
    
class UserLogin(View):
    def get(self,request,*args, **kwargs):
        form=UserLoginForm()
        return render(request,'user_login.html',{'form':form})
    
    def post(self,request,*args, **kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return render(request,'user_index.html')
        else:
            form=UserLoginForm()
            return render(request,'user_login.html',{'form':form})

class UserLogout(View):
    def get(self,request):
        logout(request)
        return redirect('enter_home')
            

class UserHome(TemplateView):
    template_name='user_index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user=self.request.user
        context["user"] = user
        return context
    
    
class CarsView(TemplateView):
    template_name='user_cars.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cars=CarCategory.objects.all()
        context['cars']=cars
        return context
    
class CarDetailView(DetailView):
     model=CarCategory
     template_name='user_car_detail.html'
     pk_url_kwarg='id'
     context_object_name="car"

class AccessCarView(TemplateView):
    template_name='access_car_index.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cars=CarCategory.objects.all()
        context['cars']=cars
        return context
 
class AdminPanel(TemplateView):
    template_name='admin_panel.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cars=CarCategory.objects.all()
        context['cars']=cars
        return context


class AdminCarView(TemplateView):
    template_name='admin_car.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cars=CarCategory.objects.all()
        context['cars']=cars
        return context

class AdminCarDetailView(DetailView):
    model=CarCategory
    template_name='admin_car_detail.html'
    pk_url_kwarg='id'
    context_object_name="car"

class AdminCarDeleteView(DeleteView):
    model=CarCategory
    success_url=reverse_lazy('admin_car')
    pk_url_kwarg='id'
    template_name='admin_car_delete.html'    

class CarBookingView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get('id')
        car=CarCategory.objects.get(id=id)
        form=CarBookingForm()
        return render(request,'user_car_book.html',{'car':car,'form':form})
    
    def post(self,request,*args, **kwargs):
        user=request.user
        id=kwargs.get('id')
        name=CarCategory.objects.get(id=id)
        price=CarCategory.objects.get(id=id)
        renter=request.POST['renter']
        place=request.POST['place']
        contact=request.POST['contact'] 
        duration=int(request.POST.get('duration'))
        total=float(duration*(name.price))
        pd=request.POST['pd']
        CarBooking.objects.create(user=user,name=name,price=price,renter=renter,place=place,contact=contact,duration=duration,total=total,pd=pd)
        return redirect('user_home')
    
class AdminCarEditView(UpdateView):
        form_class=CarEditForm
        model=CarCategory
        template_name='admin_car_edit.html'
        success_url=reverse_lazy('admin_car')
        pk_url_kwarg='id'

class AdminCarAddView(CreateView):
    template_name='admin_car_add.html'
    model=CarCategory
    form_class=CarEditForm
    
    def form_valid(self, form):
        CarCategory.objects.create(**form.cleaned_data)
        return redirect('admin_car')

class UserBookings(ListView):
    template_name='user_booking.html'
    model=CarBooking
    context_object_name='bookings'
    
    def get_queryset(self):
        return CarBooking.objects.filter(user=self.request.user)

class DeleteBooking(DeleteView):
    model=CarBooking
    success_url=reverse_lazy('user_bookings')
    pk_url_kwarg='id'
    template_name='user_order_delete.html'

class UserProfileView(DetailView):
    model=User
    template_name='user_profile_view.html'
    pk_url_kwarg='id'
    context_object_name='user'
    
class UserPersonalDetails(CreateView):
    template_name='user_personal_detail_view.html'
    model=UserPersonalInfo
    form_class=UserPersonalInfoForm
    
    def form_valid(self, form):
        UserPersonalInfo.objects.create(user=self.request.user,**form.cleaned_data)
        return redirect('user_home')
    
class UserProfileList(ListView):
    model=UserPersonalInfo
    template_name='user_profile_view2.html'
    context_object_name='userpro'
    
    def get_queryset(self):
        return UserPersonalInfo.objects.filter(user=self.request.user)
    
class UserEditView(UpdateView):
    model=UserPersonalInfo
    form_class=UserPersonalInfoForm
    pk_url_kwarg='id'
    template_name='user_profile_edit_view.html'
    success_url=reverse_lazy('user_pro_view')
    
class BlogCreateView(CreateView):
    template_name='userblog_create.html'
    model=BlogModels
    form_class=BlogForm
    
    def form_valid(self, form):
        BlogModels.objects.create(user=self.request.user,**form.cleaned_data)
        return redirect('user_blog_view')

class BlogListUserView(ListView):
    template_name='userblog.html'
    model=BlogModels
    context_object_name='blog'
    
    def get_queryset(self):
        return BlogModels.objects.all()

class BlogListAccessView(ListView):
    template_name='accessblog.html'
    model=BlogModels
    context_object_name='blog'
    
    def get_queryset(self):
        return BlogModels.objects.all() 

class UserMessageView(CreateView):
    template_name='user_message.html'
    model=UserMessagesModel
    form_class=UserMessageForm
    
    def form_valid(self, form):
        UserMessagesModel.objects.create(user=self.request.user,**form.cleaned_data)
        return redirect('user_home')

class CarSedanView(TemplateView):
    template_name='user_1_sedan.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cars=CarCategory.objects.filter(Type='sedan')
        context['cars']=cars
        return context
    
    
class CarHBView(TemplateView):
    template_name='user_2_hb.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cars=CarCategory.objects.filter(Type='hatchback')
        context['cars']=cars
        return context
    
    
class CarSUVView(TemplateView):
    template_name='user_3_suv.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars=CarCategory.objects.filter(Type='suv')
        context["cars"]=cars
        return context
    
class CarPickupView(TemplateView):
    template_name='user_4_pickup.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars=CarCategory.objects.filter(Type='pickup')
        context["cars"] = cars
        return context
    

class CarConView(TemplateView):
    template_name='user_5_con.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars=CarCategory.objects.filter(Type='convertable')
        context["cars"] = cars
        return context
    
    
class CarVanView(TemplateView):
    template_name='user_6_van.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars=CarCategory.objects.filter(Type='van')
        context["cars"] = cars
        return context
    

class CarWagonView(TemplateView):
    template_name='user_7_wagon.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars=CarCategory.objects.filter(Type='wagon')
        context["cars"] = cars
        return context

class CarCoupeView(TemplateView):
    template_name='user_8_coupe.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars=CarCategory.objects.filter(Type='coupe')
        context["cars"] = cars
        return context
    
class AddLocationView(CreateView):
    template_name='add_locations.html'
    model=LocationsModel
    form_class=LocationForm
    
    def form_valid(self, form):
        LocationsModel.objects.create(**form.cleaned_data)
        return redirect('admin')

class LocationsView(TemplateView):
    template_name='locations.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loc=LocationsModel.objects.all()
        context["loc"] = loc
        return context

class UserMails(ListView):
    template_name='user_mails.html'
    model=UserMessagesModel
    context_object_name='mail'
    
    def get_queryset(self):
        return UserMessagesModel.objects.all()
    

class AdminMailReplay(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get('id')
        mail=UserMessagesModel.objects.get(id=id)
        return render(request,'send_mail.html',{'mail':mail})
    
    def post(self,request,*args, **kwargs):
        id=kwargs.get('id')
        mail=UserMessagesModel.objects.get(id=id)
        to_mail=mail.email
        sub=mail.message
        mes=request.POST['message']
        
        res=send_mail(sub,mes,settings.EMAIL_HOST_USER,[to_mail])
        
        if res==1:
            return HttpResponse("<script>alert('success');</script>")
            # msg='Mail sent successfully'
        else:
            # msg='Faild'
            return HttpResponse("<script>alert('faild');</script>")