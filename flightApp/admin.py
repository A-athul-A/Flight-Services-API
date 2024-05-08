from django.contrib import admin
from . models import Flight,Passenger,Reservation
# Register your models here.
db = Flight,Passenger,Reservation

admin.site.register(db)