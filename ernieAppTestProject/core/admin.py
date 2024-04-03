from django.contrib import admin
from django.contrib import admin
from .models import Bus, Driver, SeatReservation

# Register your models here.


admin.site.register(Bus)
admin.site.register(Driver)
admin.site.register(SeatReservation)
