from django.shortcuts import render
from rest_framework.response import Response
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Flight, Passenger, Reservation
from rest_framework import filters
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    filter_backend=[filters.SearchFilter]
    search_fields=['departureCity', 'arrivalCity', 'dateOfDeparture']
    permission_classes=(IsAuthenticated,)

class PassengerViewSet(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    permission_classes=(IsAuthenticated,)

@api_view(['POST'])
def reservation_operations(request):
    if request.method=='POST':
        flight=Flight.objects.filter(departureCity=request.data ['departureCity'], arrivalCity=request.data['arrivalCity'], dateOfDeparture=request.data['dateOfDeparture'])
        serializer=FlightSerializer(flight)
        return Response(serializer.data)
    else:
        serializer=FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def save_reservation(request):
    flight=Flight.objects.get(id=request.data['flightId'])
    passenger=Passenger()
    passenger.firstName=request.data['firstName']
    passenger.middleName=request.data['middleName']
    passenger.lastName=request.data['lastName']
    passenger.email=request.data['email']
    passenger.phone=request.data['phone']
    passenger.save()

    reservation=Reservation()
    reservation.flight=flight
    reservation.passenger=passenger
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def find_flight(request):
    flights=Flight.objects.filter(departureCity=request.data['departureCity'])
    serializer=FlightSerializer(flights, many=True)
    return Response(serializer.data)