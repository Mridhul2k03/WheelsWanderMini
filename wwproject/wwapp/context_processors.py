from wwapp.models import CarBooking

def booking_count(request):
    if request.user.is_authenticated:
        count=CarBooking.objects.filter(user=request.user).count()
        return{'count':count}
    else:
        return{'count':0}