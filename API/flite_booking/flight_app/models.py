from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber=models.CharField(max_length=50)
    operatingAirlines=models.CharField(max_length=50)
    departureCity=models.CharField(max_length=50)
    arrivalCity=models.CharField(max_length=50)
    dateOfDeparture=models.DateField()
    estimatedTimeOfDeparture=models.TimeField()

    def __str__(self):
        return self.flightNumber

class Passenger(models.Model):
    firstName=models.CharField(max_length=50)
    middleName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=12)

    def __str__(self):
        return self.firstName

class Reservation(models.Model):
    flight=models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger=models.OneToOneField(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return self.passenger.firstName