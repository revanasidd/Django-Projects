from rest_framework import serializers
from.models import Flight, Passenger, Reservation

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields=['flightNumber', 'operatingAirlines', 'departureCity', 'arrivalCity', 'dateOfDeparture', 'estimatedTimeOfDeparture']

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields=['firstName', 'middleName', 'lastName', 'email', 'phone']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields=['flight', 'passenger']