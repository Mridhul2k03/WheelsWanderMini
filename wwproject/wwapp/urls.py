from django.urls import path
from wwapp import views

urlpatterns = [
    path('',views.AccessHome.as_view(),name='enter_home'),
    path('Register',views.UserRegister.as_view(),name="reg_view"),
    path('log/admin',views.Adminlogin.as_view(), name="admin_login"),
    path('login',views.UserLogin.as_view(),name='log_view'),
    path('userhome',views.UserHome.as_view(),name='user_home'),
    path('logouted',views.UserLogout.as_view(),name='logout_view'),
    path('car/',views.CarsView.as_view(),name='carslist_view'),
    path('details/<int:id>',views.CarDetailView.as_view(),name='car_detail_view'),
    path('userprofile/<int:id>',views.UserProfileView.as_view(),name='user_profile_view'),
    path('admin',views.AdminPanel.as_view(),name='admin'),
    path('admincar',views.AdminCarView.as_view(),name='admin_car'),
    path('bookcar/<int:id>',views.CarBookingView.as_view(),name="car_book_view"),
    path('access/car',views.AccessCarView.as_view(),name='access_car'),
    path('admincardetail/<int:id>',views.AdminCarDetailView.as_view(),name='admincard_view'),
    path('admincardelete/<int:id>',views.AdminCarDeleteView.as_view(),name='admin_car_delete_view'),
    path('adminedit/<int:id>',views.AdminCarEditView.as_view(),name='admin_car_edit'),
    path('admincaradd',views.AdminCarAddView.as_view(),name='admin_car_add'),
    path('bookings',views.UserBookings.as_view(),name='user_bookings'),
    path('bookig/delete/<int:id>',views.DeleteBooking.as_view(),name='delete_booking'),
    path('profile/<int:id>',views.UserPersonalDetails.as_view(),name='user_detail_view'),
    path('blog/',views.BlogCreateView.as_view(),name='blog_create_view'),
    path('userblog/',views.BlogListUserView.as_view(),name='user_blog_view'),
    path('profilemain',views.UserProfileList.as_view(),name='user_pro_view'),
    path('blog/main',views.BlogListAccessView.as_view(),name='blog_access'),
    path('contact/nl',views.UserMessageView.as_view(),name='user_message'),
    path('car/sedan',views.CarSedanView.as_view(),name='sedan_view'),
    path('car/hatchback',views.CarHBView.as_view(),name='hatch_view'),
    path('car/suv',views.CarSUVView.as_view(),name='suv_view'),
    path('car/pickup',views.CarPickupView.as_view(),name='pickup_view'),
    path('car/convertable',views.CarConView.as_view(),name='con_view'),
    path('car/van',views.CarVanView.as_view(),name='van_view'),
    path('car/wagon',views.CarWagonView.as_view(),name='wagon_view'),
    path('car/coupe',views.CarCoupeView.as_view(),name='coupe_view'),
    path('add/location/',views.AddLocationView.as_view(),name='add_location_view'),
    path('locations',views.LocationsView.as_view(),name='location_view'),
    path('user/proedit/<int:id>',views.UserEditView.as_view(),name='user_pro_edit_view'),
    path('mails',views.UserMails.as_view(),name='mails_view'),
    path('replaymain/<int:id>',views.AdminMailReplay.as_view(),name='admin_replay'),
    # path('payment/',views.homepage,name='payment')
]