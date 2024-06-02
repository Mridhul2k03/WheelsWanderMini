from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CarCategory(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100,null=True,blank=True)
    options=(
        ('premium','premium'),
        ('vintage','vintage')
    )
    category=models.CharField(max_length=100,choices=options)
    options=(
        ('sedan','sedan'),
        ('hatchback','hatchback'),
        ('suv','suv'),
        ('coupe','coupe'),
        ('pickup','pickup'),
        ('convertable','convertable'),
        ('van','van'),
        ('wagon','wagon')
    )
    Type=models.CharField(max_length=100,choices=options)
    brand=models.CharField(max_length=50)
    fuel_option=(
        ('petrol','petrol'),
        ('diesel','diesel'),
        ('electric','electric')
    )
    fuel=models.CharField(max_length=100,choices=fuel_option)
    gear_options=(
        ('Manuel','Manuel'),
        ('Automatic','Automatic')
    )
    transmission=models.CharField(max_length=50,choices=gear_options)
    image_black=models.ImageField(upload_to='car_images_1',null=True,blank=True)
    image_white=models.ImageField(upload_to='car_images_2',null=True,blank=True)
    image_red=models.ImageField(upload_to='car_images_3',null=True,blank=True)
    image_blue=models.ImageField(upload_to='car_images_4',null=True,blank=True)
    image_green=models.ImageField(upload_to='car_images_5',null=True,blank=True)
    milage=models.CharField(max_length=50)
    price=models.IntegerField()
    duration=models.CharField(max_length=100,default='Per Day')
    status=models.BooleanField(default=True)
    exclusive=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
        
class LocationsModel(models.Model):
    options=(
        ('trivandram','trivandram'),
        ('kollam','kollam'),
        ('alappuzha','alappuzha'),
        ('pathanamthitta','pathanamthitta'),
        ('kottayam','kottayam'),
        ('idukki','idukki'),
        ('ernakulam','eranakulam'),
        ('thrissur','thrissur'),
        ('palakkad','palakkad'),
        ('malappuram','malappuram'),
        ('kozhikode','kozhikode'),
        ('wayanad','wayanad'),
        ('kannur','kannur'),
        ('kasargod','kasargod')
    )
    place=models.CharField(max_length=100,choices=options,default='kozhikode')
    link=models.URLField(max_length=500)
    area=models.CharField(max_length=100)


class CarBooking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.ForeignKey(CarCategory, on_delete=models.CASCADE, related_name='car_bookings_name')
    renter=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    contact=models.CharField(max_length=50)
    duration=models.IntegerField(null=True)
    total=models.CharField(max_length=50,null=False,blank=False)
    price=models.ForeignKey(CarCategory, on_delete=models.CASCADE, related_name='car_bookings_price',null=True)
    pd=models.DateField()
    
    def __str__(self):
        return self.renter
    
class UserPersonalInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='user_image')
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    phone=models.PositiveIntegerField()
    dob=models.DateField()
    options=(
        ('single','single'),
        ('marrid','married')
    )
    status=models.CharField(max_length=50,choices=options)
    options=(
        ('male','male'),
        ('female','female')
    )
    gender=models.CharField(max_length=100,choices=options)
    
class BlogModels(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='bloguser')
    image=models.ImageField(upload_to='blog_images',null=True,blank=True)
    description=models.CharField( max_length=1000,null=True,blank=True)
    options=(
        (0,'0'),
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')
    )
    rating=models.PositiveIntegerField(null=True, blank=True,choices=options)

class UserMessagesModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=500)


    